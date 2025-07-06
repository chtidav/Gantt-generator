@echo off
chcp 65001 >nul
title Gantt Chart Generator

:start
cls
echo.
echo ===============================================
echo   📊 GANTT CHART GENERATOR
echo ===============================================
echo.
echo Choose an action:
echo.
echo 1. 🆕 Create new diagram
echo 2. 📂 Load existing configuration
echo 3. 🔍 Extract from existing HTML
echo 4. 🧪 Test extractor
echo 5. 📚 Documentation
echo 6. 🚪 Exit
echo.

set /p "choice=Your choice (1-6): "

if "%choice%"=="1" goto nouveau
if "%choice%"=="2" goto charger
if "%choice%"=="3" goto extraire
if "%choice%"=="4" goto tester
if "%choice%"=="5" goto docs
if "%choice%"=="6" goto quitter
goto invalid

:nouveau
echo.
echo 🆕 Creating new diagram...
echo.
python "%~dp0..\src\gantt_generator.py"
goto fin

:charger
echo.
echo 📂 Loading configuration...
echo.
python "%~dp0..\src\gantt_generator.py"
goto fin

:extraire
echo.
echo 🔍 Extracting from HTML...
echo.
python "%~dp0..\src\gantt_extractor.py"
goto fin

:tester
echo.
echo 🧪 Testing extractor...
echo.
python "%~dp0..\src\test_extractor.py"
goto fin

:docs
echo.
echo 📚 Available documentation:
echo.
echo - user_guide.md         : Complete user guide
echo - extractor_guide.md    : Extractor documentation  
echo - styling_guide.md      : Template styling guide
echo.
echo These files contain all necessary documentation.
echo.
goto fin

:invalid
echo.
echo ❌ Invalid choice. Please enter a number between 1 and 6.
echo.
pause
goto start

:quitter
echo.
echo 👋 Goodbye!
goto end

:fin
echo.
echo Press any key to return to menu...
pause >nul
goto start

:end
