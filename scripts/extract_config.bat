@echo off
chcp 65001 >nul
title Extracteur de Configuration Gantt

echo.
echo ===============================================
echo   🔍 EXTRACTEUR DE CONFIGURATION GANTT
echo ===============================================
echo.
echo Ce script analyse un fichier HTML de diagramme
echo de Gantt et génère sa configuration JSON.
echo.

REM Vérifier si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python n'est pas installé ou accessible.
    echo Veuillez installer Python depuis https://python.org/
    pause
    exit /b 1
)

REM Aller dans le répertoire du script
cd /d "%~dp0"

echo 🐍 Lancement de l'extracteur Python...
echo.

REM Lancer l'extracteur Python
python gantt_extractor.py %*

if errorlevel 1 (
    echo.
    echo ❌ Une erreur s'est produite lors de l'extraction.
    echo.
) else (
    echo.
    echo ✅ Extraction terminée avec succès!
    echo.
)

echo Appuyez sur une touche pour fermer...
pause >nul
