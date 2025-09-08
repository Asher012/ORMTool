# ReviewForge Analytics Pro Enhanced - Setup Guide

## 🚀 Installation Instructions

### Prerequisites
- Python 3.9 or higher
- Git (optional)
- Chrome browser (for web scraping)

### Step 1: Clone or Download
```bash
# If using Git
git clone <repository-url>
cd reviewforge-enhanced

# Or download the files manually and extract to a folder
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv reviewforge_env

# Activate virtual environment
# Windows:
reviewforge_env\Scripts\activate

# macOS/Linux:
source reviewforge_env/bin/activate
```

### Step 3: Install Dependencies
```bash
# Install all required packages
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Download NLTK data (run this once)
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

### Step 4: Run the Application
```bash
streamlit run reviewforge-pro-enhanced.py
```

## 🔧 Configuration

### Default Login Credentials
- Username: `admin`
- Password: `admin123`

**Important: Change these credentials immediately after first login!**

### Google My Business Setup
1. The GMB scraper uses Playwright/Selenium
2. Make sure Chrome browser is installed
3. For best results, use the Playwright method

### Webhook Integration

#### Slack Webhook Setup:
1. Go to https://api.slack.com/apps
2. Create a new app or use existing
3. Go to "Incoming Webhooks" and activate
4. Create webhook for desired channel
5. Copy the webhook URL and paste in the app

#### Discord Webhook Setup:
1. Open Discord server settings
2. Go to Integrations > Webhooks
3. Create New Webhook
4. Copy webhook URL and paste in the app

### Google Sheets Integration
1. Go to Google Cloud Console
2. Create a new project or select existing
3. Enable Google Sheets API and Google Drive API
4. Create Service Account credentials
5. Download JSON key file
6. Upload the JSON file in the app's Google Sheets section

## 📊 Features Overview

### Core Features:
- ✅ Google Play Store review analysis
- ✅ Google My Business review extraction
- ✅ Advanced sentiment analysis
- ✅ Secure user authentication
- ✅ Real-time webhook notifications (Slack/Discord)
- ✅ Google Sheets integration
- ✅ Automated monitoring and scheduling
- ✅ Multi-format export (CSV, Excel, JSON)
- ✅ Modern responsive UI
- ✅ Role-based access control

### New Enhanced Features:
1. **Google My Business Support**: Extract and analyze GMB reviews
2. **Secure Authentication**: SQLite-based user management with session tokens
3. **Webhook Notifications**: Real-time alerts to Slack/Discord
4. **Automation Scheduler**: Automated review monitoring with customizable intervals
5. **Google Sheets Integration**: Auto-export data to spreadsheets
6. **Enhanced UI**: Modern gradient design with better UX
7. **Multi-Platform Analysis**: Support for both Play Store and GMB

## 🤖 Automation Setup

### Automated Review Monitoring:
1. Configure webhooks (Slack/Discord)
2. Set up Google Sheets integration (optional)
3. Go to Automation Center
4. Add your app details and set monitoring interval
5. Click "Start Automated Monitoring"

The system will automatically:
- Check for new reviews at set intervals
- Send notifications for negative reviews
- Update Google Sheets with latest data
- Generate alerts for significant changes

## 🛠 Troubleshooting

### Common Issues:

1. **Import Errors**:
   ```bash
   pip install --upgrade -r requirements.txt
   ```

2. **Playwright Issues**:
   ```bash
   playwright install --with-deps chromium
   ```

3. **SQLite Database Issues**:
   - Delete `reviewforge_users.db` file to reset users
   - Restart the application

4. **GMB Scraping Issues**:
   - Try switching between Playwright and Selenium methods
   - Check if the GMB URL is accessible
   - Some locations may have anti-scraping measures

5. **Webhook Not Working**:
   - Verify webhook URLs are correct
   - Check if webhooks are properly configured in Slack/Discord
   - Test with the "Test Notification" buttons

## 📱 Usage Tips

### For Google My Business:
- Use the full Google search URL or Maps URL
- GMB URLs look like: `https://www.google.com/search?q=BusinessName&stick=...`
- Start with smaller review counts (50-100) for testing

### For Play Store:
- Use either the full URL or just the package name
- Package names look like: `com.company.appname`
- Higher review counts provide better insights but take longer

### For Automation:
- Start with longer intervals (60+ minutes) for testing
- Monitor system resources when running automation
- Use webhook notifications to stay updated without checking manually

## 🔐 Security Notes

1. **Change Default Password**: Immediately change admin password
2. **Webhook URLs**: Keep webhook URLs secure and don't share publicly
3. **Google Credentials**: Store Google Service Account JSON securely
4. **Database**: The SQLite database contains user credentials
5. **Network**: Consider using HTTPS in production

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify all dependencies are installed correctly
3. Ensure you have proper permissions for file operations
4. Check browser compatibility for web scraping features

## 🔄 Updates

To update the application:
1. Backup your database and settings
2. Download new version
3. Run `pip install -r requirements.txt` to update dependencies
4. Restart the application

---

**Developer**: Ayush Pandey  
**Version**: 3.0.0 Pro Enhanced  
**Last Updated**: December 2024