#!/bin/bash

# ReviewForge Analytics Pro - Quick Setup Script
# This script automates the setup process for the application

echo "========================================="
echo "ReviewForge Analytics Pro - Quick Setup"
echo "Enterprise Review Intelligence Platform"
echo "========================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.9 or higher."
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "Detected Python version: $python_version"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv reviewforge_env

# Activate virtual environment
echo "Activating virtual environment..."
source reviewforge_env/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt

# Download NLTK data
echo "Downloading NLTK data..."
python3 -c "
import nltk
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
    print('NLTK data downloaded successfully')
except:
    print('NLTK data download failed - will try again at runtime')
"

echo ""
echo "========================================="
echo "Setup Complete!"
echo "========================================="
echo ""
echo "To start the application:"
echo "1. Activate virtual environment: source reviewforge_env/bin/activate"
echo "2. Run application: streamlit run reviewforge-analytics-pro.py"
echo "3. Open browser to: http://localhost:8501"
echo ""
echo "Default login credentials:"
echo "Username: admin"
echo "Password: ReviewForge2024!"
echo ""
echo "Important: Change the default password immediately after first login!"
echo ""
echo "For detailed instructions, see DEPLOYMENT-GUIDE.md"
echo "========================================="