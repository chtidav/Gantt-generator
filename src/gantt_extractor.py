#!/usr/bin/env python3
"""
Extracteur de Configuration Gantt
Analyse un fichier HTML de diagramme de Gantt et génère sa configuration JSON

Usage:
    python gantt_extractor.py fichier.html
    python gantt_extractor.py  # Mode interactif
"""

import json
import os
import re
import sys
from bs4 import BeautifulSoup
from typing import List, Dict, Any, Optional

class GanttExtractor:
    def __init__(self):
        self.config = {
            "title": "",
            "subtitle": "",
            "periods": 0,
            "period_type": "months",
            "milestone_labels_visible": True,
            "period_labels": [],
            "rows": []
        }
        
    def extract_from_html(self, html_file: str) -> Dict[str, Any]:
        """Extrait la configuration depuis un fichier HTML"""
        
        if not os.path.exists(html_file):
            raise FileNotFoundError(f"Fichier non trouvé: {html_file}")
            
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        # D'abord, essayer d'extraire depuis la config JavaScript
        if self.extract_from_js_config(html_content):
            print("✅ Configuration extraite depuis le JavaScript")
            return self.config
            
        # Sinon, utiliser l'extraction DOM traditionnelle
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extraire les méta-informations
        self.extract_meta_info(soup, html_content)
        
        # Extraire les périodes
        self.extract_periods(soup, html_content)
        
        # Extraire les lignes
        self.extract_rows(soup)
        
        return self.config
        
    def extract_from_js_config(self, html_content: str) -> bool:
        """Tente d'extraire la configuration depuis const config = {...}"""
        
        # Chercher la déclaration de config
        config_match = re.search(r'const config = ({.*?});', html_content, re.DOTALL)
        
        if config_match:
            try:
                config_str = config_match.group(1)
                
                # Parser le JSON directement (les caractères Unicode sont déjà corrects)
                js_config = json.loads(config_str)
                
                # Copier les champs de base
                self.config["title"] = js_config.get("title", "Diagramme de Gantt")
                self.config["subtitle"] = js_config.get("subtitle", "Planning de projet")
                self.config["periods"] = js_config.get("periods", 0)
                self.config["period_type"] = js_config.get("period_type", "months")
                self.config["milestone_labels_visible"] = js_config.get("milestone_labels_visible", True)
                self.config["period_labels"] = js_config.get("period_labels", [])
                self.config["rows"] = js_config.get("rows", [])
                
                return True
                
            except json.JSONDecodeError as e:
                print(f"⚠️ Erreur lors du parsing de la config JS: {e}")
                return False
                
        return False
        
    def extract_meta_info(self, soup: BeautifulSoup, html_content: str):
        """Extrait le titre et la description"""
        
        # Titre principal
        title_elem = soup.find('h1')
        if title_elem:
            self.config["title"] = title_elem.get_text().strip()
        else:
            # Fallback sur le title de la page
            title_elem = soup.find('title')
            if title_elem:
                self.config["title"] = title_elem.get_text().strip()
            else:
                self.config["title"] = "Diagramme de Gantt"
                
        # Sous-titre/description
        subtitle_elem = soup.find('p', class_='text-gray-500')
        if subtitle_elem:
            self.config["subtitle"] = subtitle_elem.get_text().strip()
        else:
            self.config["subtitle"] = "Planning de projet"
            
    def extract_periods(self, soup: BeautifulSoup, html_content: str):
        """Extrait les informations sur les périodes"""
        
        # Chercher dans le JavaScript pour les labels de périodes
        script_match = re.search(r'const timeLabels = (\[.*?\]);', html_content, re.DOTALL)
        
        if script_match:
            # Configuration avec tableau défini
            try:
                labels_str = script_match.group(1)
                self.config["period_labels"] = json.loads(labels_str)
                self.config["periods"] = len(self.config["period_labels"])
            except json.JSONDecodeError:
                # Fallback si le parsing JSON échoue
                self.extract_periods_from_dom(soup)
        else:
            # Chercher la génération de boucle pour M1, M2, etc.
            loop_match = re.search(r'for\s*\(\s*let\s+i\s*=\s*1;\s*i\s*<=\s*(\d+);\s*i\+\+\)', html_content)
            if loop_match:
                periods_count = int(loop_match.group(1))
                self.config["periods"] = periods_count
                
                # Déterminer le type de période basé sur le pattern
                if 'M${i}' in html_content:
                    self.config["period_type"] = "months"
                    self.config["period_labels"] = [f"M{i}" for i in range(1, periods_count + 1)]
                elif 'S${i}' in html_content:
                    self.config["period_type"] = "weeks"
                    self.config["period_labels"] = [f"S{i}" for i in range(1, periods_count + 1)]
                elif 'Q${i}' in html_content:
                    self.config["period_type"] = "quarters"
                    self.config["period_labels"] = [f"Q{i}" for i in range(1, periods_count + 1)]
                else:
                    self.config["period_type"] = "custom"
                    self.config["period_labels"] = [f"P{i}" for i in range(1, periods_count + 1)]
            else:
                # Fallback: compter les colonnes dans l'en-tête
                self.extract_periods_from_dom(soup)
                
        # Détecter le type de période basé sur les labels
        if self.config["period_labels"]:
            first_label = self.config["period_labels"][0]
            if first_label.startswith('M'):
                self.config["period_type"] = "months"
            elif first_label.startswith('S'):
                self.config["period_type"] = "weeks"
            elif first_label.startswith('Q'):
                self.config["period_type"] = "quarters"
            else:
                self.config["period_type"] = "custom"
                
    def extract_periods_from_dom(self, soup: BeautifulSoup):
        """Extrait les périodes depuis le DOM"""
        
        header = soup.find('div', class_='gantt-header')
        if header:
            # Compter les cellules avec du texte (ignorer la cellule vide de fin)
            cells = header.find_all('div')
            period_cells = [cell for cell in cells if cell.get_text().strip() and not cell.get('class')]
            
            if period_cells:
                self.config["period_labels"] = [cell.get_text().strip() for cell in period_cells]
                self.config["periods"] = len(self.config["period_labels"])
            else:
                # Fallback par défaut
                self.config["periods"] = 24
                self.config["period_labels"] = [f"M{i}" for i in range(1, 25)]
                
    def extract_rows(self, soup: BeautifulSoup):
        """Extrait toutes les lignes du diagramme"""
        
        # Trouver toutes les paires label + container
        labels = soup.find_all('div', class_='gantt-row-label')
        
        for label_elem in labels:
            # Ignorer l'en-tête
            if 'gantt-row-label-header' in label_elem.get('class', []):
                continue
                
            row_name = label_elem.get_text().strip()
            if not row_name:
                continue
                
            # Trouver le container associé (élément suivant)
            container = label_elem.find_next_sibling()
            if not container:
                continue
                
            row = self.extract_single_row(row_name, container)
            if row:
                self.config["rows"].append(row)
                
    def extract_single_row(self, name: str, container) -> Optional[Dict[str, Any]]:
        """Extrait une ligne individuelle"""
        
        # Déterminer le type de ligne
        container_classes = container.get('class', [])
        
        # Vérifier s'il y a des éléments de recrutement
        has_recruitment = container.find_all('div', class_='recruitment-item')
        
        if 'gantt-bar-container-simple' in container_classes:
            row_type = "simple"
        elif has_recruitment or 'recruitment-row' in container_classes:
            row_type = "special"
        elif 'special-row' in container_classes:
            row_type = "special" 
        else:
            row_type = "milestones"  # Par défaut si c'est gantt-bar-container
            
        row = {
            "name": name,
            "type": row_type,
            "tasks": [],
            "milestones": [],
            "special_items": []
        }
        
        # Extraire les tâches
        self.extract_tasks(container, row)
        
        # Extraire les jalons si applicable
        if row_type == "milestones":
            self.extract_milestones(container, row)
            
        # Extraire les éléments spéciaux si applicable
        if row_type == "special":
            self.extract_special_items(container, row)
            
        return row
        
    def extract_tasks(self, container, row: Dict[str, Any]):
        """Extrait les tâches d'un container"""
        
        task_bars = container.find_all('div', class_='gantt-bar')
        
        for bar in task_bars:
            task_name = bar.get_text().strip()
            if not task_name:
                continue
                
            # Extraire le positionnement depuis le style
            style = bar.get('style', '')
            grid_match = re.search(r'grid-column:\s*(\d+)\s*/\s*span\s*(\d+)', style)
            
            if grid_match:
                start = int(grid_match.group(1))
                duration = int(grid_match.group(2))
                
                # Déterminer le style CSS
                css_classes = bar.get('class', [])
                style_class = self.determine_task_style(css_classes)
                
                row["tasks"].append({
                    "name": task_name,
                    "start": start,
                    "duration": duration,
                    "style": style_class
                })
                
    def determine_task_style(self, css_classes: List[str]) -> str:
        """Détermine le style d'une tâche basé sur ses classes CSS"""
        
        # Construire le style complet en combinant les classes de couleur
        bg_class = None
        text_class = None
        
        # Chercher les classes de fond et de texte
        for css_class in css_classes:
            if css_class.startswith('bg-'):
                bg_class = css_class
            elif css_class.startswith('text-'):
                text_class = css_class
        
        # Si on a trouvé un fond et un texte, retourner la combinaison
        if bg_class and text_class:
            return f"{bg_class} {text_class}"
        elif bg_class:
            # Pour les phases, ajouter text-white par défaut
            if bg_class in ['bg-sky-500', 'bg-amber-500', 'bg-emerald-500']:
                return f"{bg_class} text-white"
            # Pour les tâches, déduire la couleur de texte
            elif bg_class == 'bg-sky-100':
                return f"{bg_class} text-sky-800"
            elif bg_class == 'bg-amber-100':
                return f"{bg_class} text-amber-800"
            elif bg_class == 'bg-emerald-100':
                return f"{bg_class} text-emerald-800"
            else:
                return bg_class
            
        # Fallback sur les styles abstraits
        if 'phase-1' in css_classes:
            return 'bg-sky-500 text-white'
        elif 'phase-2' in css_classes:
            return 'bg-amber-500 text-white'
        elif 'phase-3' in css_classes:
            return 'bg-emerald-500 text-white'
        elif 'task-primary' in css_classes:
            return 'bg-sky-100 text-sky-800'
        elif 'task-secondary' in css_classes:
            return 'bg-amber-100 text-amber-800'
        elif 'task-success' in css_classes:
            return 'bg-emerald-100 text-emerald-800'
            
        # Fallback par défaut
        return 'bg-sky-100 text-sky-800'
        
    def extract_milestones(self, container, row: Dict[str, Any]):
        """Extrait les jalons d'un container"""
        
        # Chercher les divs avec positionnement de grille qui contiennent des jalons
        milestone_containers = container.find_all('div', style=re.compile(r'grid-column:\s*\d+'))
        
        for milestone_container in milestone_containers:
            # Vérifier si c'est bien un jalon
            milestone_div = milestone_container.find('div', class_='milestone')
            if not milestone_div:
                continue
                
            # Extraire le nom du jalon
            label_elem = milestone_div.find('div', class_='milestone-label')
            if not label_elem:
                continue
                
            milestone_name = label_elem.get_text().strip()
            
            # Extraire la colonne depuis le style
            style = milestone_container.get('style', '')
            column_match = re.search(r'grid-column:\s*(\d+)', style)
            
            if column_match:
                column = int(column_match.group(1))
                
                # Déterminer si c'est un jalon de fin
                is_end = column > self.config["periods"] or 'milestone-end' in milestone_div.get('class', [])
                
                row["milestones"].append({
                    "name": milestone_name,
                    "column": column,
                    "is_end": is_end
                })
                
    def extract_special_items(self, container, row: Dict[str, Any]):
        """Extrait les éléments spéciaux d'un container"""
        
        # Chercher les éléments spéciaux (tous types)
        special_items = container.find_all('div', class_=['recruitment-item', 'special-item'])
        
        for item in special_items:
            item_name = item.get_text().strip()
            if not item_name:
                continue
                
            # Extraire le positionnement
            style = item.get('style', '')
            
            # Grid column
            grid_match = re.search(r'grid-column:\s*(\d+)\s*/\s*span\s*(\d+)', style)
            if not grid_match:
                continue
                
            start = int(grid_match.group(1))
            duration = int(grid_match.group(2))
            
            # Position verticale
            position = "top"  # par défaut
            if 'bottom:' in style:
                position = "bottom"
            elif 'top:' in style:
                position = "top"
            
            # Extraire le style CSS de l'élément
            css_classes = item.get('class', [])
            item_style = ' '.join(css_classes) if css_classes else 'special-item'
                
            row["special_items"].append({
                "name": item_name,
                "start": start,
                "duration": duration,
                "position": position,
                "style": item_style
            })
        
        # Chercher les autres éléments spéciaux
        special_items = container.find_all('div', class_='special-item')
        
        for item in special_items:
            item_name = item.get_text().strip()
            if not item_name:
                continue
                
            # Extraire le positionnement
            style = item.get('style', '')
            
            # Grid column
            grid_match = re.search(r'grid-column:\s*(\d+)\s*/\s*span\s*(\d+)', style)
            if not grid_match:
                continue
                
            start = int(grid_match.group(1))
            duration = int(grid_match.group(2))
            
            # Position verticale
            position = "top"  # par défaut
            if 'bottom:' in style:
                position = "bottom"
            elif 'top:' in style:
                position = "top"
                
            row["special_items"].append({
                "name": item_name,
                "start": start,
                "duration": duration,
                "position": position,
                "type": "special"
            })
            
    def save_config(self, output_file: str = None) -> str:
        """Sauvegarde la configuration extraite"""
        
        if not output_file:
            # Générer un nom basé sur le titre
            safe_title = re.sub(r'[^\w\-_]', '_', self.config["title"])
            output_file = f"extracted_config_{safe_title}.json"
            
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
            
        return output_file
        
    def print_summary(self):
        """Affiche un résumé de la configuration extraite"""
        
        print(f"Titre: {self.config['title']}")
        print(f"Description: {self.config['subtitle']}")
        print(f"Périodes: {self.config['periods']} ({self.config['period_type']})")
        print(f"📋 Lignes: {len(self.config['rows'])}")
        
        for i, row in enumerate(self.config['rows'], 1):
            print(f"  {i}. {row['name']} ({row['type']})")
            print(f"     - Tâches: {len(row['tasks'])}")
            if row['type'] == 'milestones':
                print(f"     - Jalons: {len(row['milestones'])}")
            elif row['type'] == 'special':
                print(f"     - Éléments spéciaux: {len(row['special_items'])}")


def main():
    """Fonction principale"""
    
    print("Extracteur de Configuration Gantt")
    print("=" * 40)
    
    # Déterminer le fichier d'entrée
    if len(sys.argv) > 1:
        html_file = sys.argv[1]
    else:
        html_file = input("📁 Chemin du fichier HTML: ").strip()
        
    if not html_file:
        print("ERREUR: Aucun fichier spécifié")
        return
        
    try:
        # Installer beautifulsoup4 si nécessaire
        try:
            from bs4 import BeautifulSoup
        except ImportError:
            print("📦 Installation de beautifulsoup4...")
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
            from bs4 import BeautifulSoup
            
        extractor = GanttExtractor()
        
        print(f"Analyse de {html_file}...")
        config = extractor.extract_from_html(html_file)
        
        print("\nExtraction terminée!")
        extractor.print_summary()
        
        # Sauvegarder la configuration
        if input("\n💾 Sauvegarder la configuration? (Y/n): ").lower() != 'n':
            output_file = extractor.save_config()
            print(f"✅ Configuration sauvegardée: {output_file}")
            
            # Proposer de générer un nouveau Gantt
            if input("\n🚀 Générer un nouveau Gantt avec cette configuration? (y/N): ").lower() == 'y':
                import subprocess
                try:
                    subprocess.run([sys.executable, "gantt_generator.py"], input="2\n" + output_file + "\n", text=True)
                except FileNotFoundError:
                    print("ERREUR: gantt_generator.py non trouvé dans le même dossier")
                    
    except FileNotFoundError as e:
        print(f"ERREUR: {e}")
    except Exception as e:
        print(f"ERREUR lors de l'extraction: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
