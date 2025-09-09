@echo off
REM ReviewForge Analytics Pro - Quick Setup Script (Windows)
REM This script automates the setup process for the application

echo =========================================
echo ReviewForge Analytics Pro - Quick Setup
echo Enterprise Review Intelligence Platform
echo =========================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed. Please install Python 3.9 or higher.
    pause
    exit /b 1
)

REM Display Python version
echo Detected Python version:
python --version

REM Create virtual environment
echo Creating virtual environment...
python -m venv reviewforge_env

REM Activate virtual environment
echo Activating virtual environment...
call reviewforge_env\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt

REM Download NLTK data
echo Downloading NLTK data...
python -c "import nltk; nltk.download('punkt', quiet=True); nltk.download('stopwords', quiet=True); nltk.download('wordnet', quiet=True); print('NLTK data downloaded successfully')" 2>nul || echo NLTK data download failed - will try again at runtime

echo.
echo =========================================
echo Setup Complete!
echo =========================================
echo.
echo To start the application:
echo 1. Activate virtual environment: reviewforge_env\Scripts\activate.bat
echo 2. Run application: streamlit run reviewforge-analytics-pro.py
echo 3. Open browser to: http://localhost:8501
echo.
echo Default login credentials:
echo Username: admin
echo Password: ReviewForge2024!
echo.
echo Important: Change the default password immediately after first login!
echo.
echo For detailed instructions, see DEPLOYMENT-GUIDE.md
echo =========================================

pause