#!/usr/bin/env python3
"""
Gantt Chart Generator
Professional timeline visualization tool
"""

import json
import os
import sys
import argparse
from datetime import datetime


class GanttGenerator:
    def __init__(self, language="en", template_path=None):
        self.language = language
        self.template_path = template_path or self.get_default_template_path()
        self.config = {
            "title": "My Project",
            "subtitle": "Project Timeline",
            "periods": 12,
            "period_type": "months",
            "period_labels": [f"M{i}" for i in range(1, 13)],
            "rows": []
        }
    
    def get_default_template_path(self):
        """Get path to default template"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(os.path.dirname(script_dir), "templates")
        return os.path.join(template_dir, "simple_template.html")
    
    def load_config_from_file(self, filepath):
        """Load configuration from JSON file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
    
    def generate_html(self, output_file=None):
        """Generate HTML file"""
        if not os.path.exists(self.template_path):
            print(f"Template not found: {self.template_path}")
            return None
        
        with open(self.template_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Replace placeholders
        html_content = html_content.replace("{{TITLE}}", self.config["title"])
        html_content = html_content.replace("{{SUBTITLE}}", self.config["subtitle"])
        html_content = html_content.replace("{{CONFIG_JSON}}", json.dumps(self.config))
        
        # Generate output filename
        if not output_file:
            safe_title = "".join(c for c in self.config["title"] if c.isalnum() or c in (' ', '-', '_')).rstrip()
            safe_title = safe_title.replace(' ', '_')
            output_file = f"gantt_{safe_title}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return output_file
    
    def open_in_browser(self, html_file):
        """Open HTML file in browser"""
        import webbrowser
        webbrowser.open(f'file://{os.path.abspath(html_file)}')


def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Gantt Chart Generator")
    parser.add_argument('--lang', choices=['en', 'fr'], default='en')
    parser.add_argument('--config', type=str, help='Configuration file')
    parser.add_argument('--template', type=str, help='Template file')
    parser.add_argument('--output', '-o', type=str, help='Output HTML file')
    
    args = parser.parse_args()
    
    generator = GanttGenerator(language=args.lang, template_path=args.template)
    
    try:
        if args.config:
            generator.load_config_from_file(args.config)
            output_file = generator.generate_html(args.output)
            if output_file:
                print(f"Generated: {output_file}")
                generator.open_in_browser(output_file)
        else:
            print("Interactive mode not implemented yet. Use --config parameter.")
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
