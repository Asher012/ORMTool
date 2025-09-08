# ReviewForge Analytics Pro Enhanced - Deployment Guide

## 🚀 Quick Start (5 Minutes)

1. **Download and Extract** the application files
2. **Open terminal** in the application folder
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```
4. **Run the application**:
   ```bash
   streamlit run reviewforge-pro-enhanced.py
   ```
5. **Open browser** to `http://localhost:8501`
6. **Login** with username: `admin`, password: `admin123`

## ✨ New Features Overview

### 🏢 Google My Business Support
- Extract reviews directly from GMB listings
- Support for both Playwright and Selenium scraping
- Automatic sentiment analysis for GMB reviews
- Real-time monitoring capabilities

### 🔐 Secure Authentication System
- SQLite database for user management
- Password hashing with Werkzeug
- Session token-based authentication
- Role-based access control (admin/user)
- Secure logout and session management

### 🤖 Automation & Webhooks
- **Slack Integration**: Real-time notifications to Slack channels
- **Discord Integration**: Automated alerts to Discord servers
- **Scheduled Monitoring**: Auto-check for new reviews at custom intervals
- **Smart Notifications**: Alerts for negative reviews and significant changes

### 📊 Google Sheets Integration
- Auto-export data to Google Sheets
- Service account-based authentication
- Real-time sheet updates
- Batch data processing

### 🎨 Enhanced User Interface
- Modern gradient design with glassmorphism effects
- Responsive layout for all screen sizes
- Interactive cards and animations
- Better navigation and user experience
- Dark/light theme elements

## 🛠 Advanced Setup

### Environment Variables (Optional)
Create a `.env` file:
```env
SECRET_KEY=your-super-secret-key-here
ENVIRONMENT=production
DATABASE_URL=sqlite:///reviewforge_users.db
```

### Google Cloud Setup for Sheets Integration
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project: "ReviewForge Analytics"
3. Enable APIs:
   - Google Sheets API
   - Google Drive API
4. Create Service Account:
   - Go to IAM & Admin > Service Accounts
   - Create new service account
   - Download JSON key file
5. Share your Google Sheets with the service account email

### Webhook Setup Guide

#### Slack Webhook:
1. Visit https://api.slack.com/apps
2. Create New App > From scratch
3. Choose workspace and app name
4. Go to Features > Incoming Webhooks
5. Activate Incoming Webhooks
6. Add New Webhook to Workspace
7. Select channel and copy webhook URL

#### Discord Webhook:
1. Open Discord server settings
2. Go to Integrations tab
3. Click "Create Webhook"
4. Choose channel and webhook name
5. Copy webhook URL

## 🔧 Configuration Options

### Analysis Settings
- **Review Count**: 100-2000 reviews per analysis
- **Sentiment Threshold**: 0.1-1.0 confidence level
- **Analysis Features**: Aspect analysis, emotion detection, topic modeling

### GMB Scraping Options
- **Method**: Playwright (recommended) or Selenium
- **Max Reviews**: 50-500 reviews per extraction
- **Timeout**: 15-60 seconds per operation

### Automation Settings
- **Monitoring Interval**: 15 minutes to 24 hours
- **Notification Types**: Negative reviews, competitor updates, system alerts
- **Auto-start**: Enable/disable automatic monitoring on startup

## 📊 Usage Examples

### Basic Play Store Analysis
1. Login to the application
2. Go to Analytics Dashboard
3. Enter Play Store URL: `https://play.google.com/store/apps/details?id=com.workindia.nitya`
4. Select review count and sort method
5. Click "Analyze Application"

### GMB Review Extraction
1. Go to Google My Business page
2. Enter GMB URL (from Google Search or Maps)
3. Choose extraction method (Playwright recommended)
4. Set max reviews (start with 50-100)
5. Click "Extract GMB Reviews"

### Setting Up Automation
1. Configure webhooks in Automation Center
2. Add Slack/Discord webhook URLs
3. Set up Google Sheets integration
4. Schedule review monitoring with custom intervals
5. Start automated monitoring

## 🚨 Important Notes

### Security Considerations
- **Change default password** immediately after first login
- **Keep webhook URLs secure** - don't share publicly
- **Use HTTPS** in production environments
- **Regular backups** of the SQLite database
- **Environment variables** for sensitive configuration

### Performance Tips
- **Start with smaller datasets** (100-500 reviews) for testing
- **Use longer intervals** for automation (30+ minutes)
- **Monitor system resources** during large analyses
- **Cache results** when possible
- **Close browser processes** after GMB scraping

### Troubleshooting Common Issues

#### Import Errors
```bash
# Fix: Update all packages
pip install --upgrade -r requirements.txt

# Fix sklearn import error
# Change line 25 in main file:
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
```

#### Database Issues
```bash
# Reset user database
rm reviewforge_users.db
# Restart application - admin user will be recreated
```

#### GMB Scraping Fails
- Try switching between Playwright and Selenium
- Check if GMB URL is publicly accessible
- Reduce max reviews count
- Try different GMB locations

#### Webhooks Not Working
- Verify webhook URLs are correct
- Test with "Test Notification" buttons
- Check webhook permissions in Slack/Discord
- Ensure internet connectivity

## 📱 Mobile Usage
- The application is responsive and works on mobile devices
- Use landscape mode for better dashboard viewing
- Touch-friendly interface elements
- Mobile-optimized data tables

## 🔄 Updates and Maintenance

### Regular Maintenance
- **Weekly**: Check automation logs and performance
- **Monthly**: Update dependencies and review security
- **Quarterly**: Database cleanup and backup
- **As needed**: Update webhook configurations

### Updating the Application
1. Backup current data and settings
2. Download new version
3. Update dependencies: `pip install -r requirements.txt`
4. Restart application
5. Verify all features work correctly

## 📞 Support and Contact

### Getting Help
1. Check this documentation first
2. Review error messages carefully
3. Test with simpler configurations
4. Check system requirements and dependencies

### Feature Requests
The application is designed to be extensible. Future enhancements may include:
- Multi-language support
- API endpoints for external integration
- Advanced machine learning models
- Custom dashboard widgets
- Enterprise SSO integration

## 🎯 Best Practices

### For Optimal Performance
- Use appropriate review counts for your needs
- Set realistic monitoring intervals
- Keep webhook notifications focused
- Regular system maintenance
- Monitor resource usage

### For Better Results
- Start with well-known apps for testing
- Use varied time periods for trend analysis
- Combine multiple data sources
- Regular competitor benchmarking
- Act on negative review insights

---

**Happy Analyzing!** 🚀

*This enhanced version brings together the best of automated review analysis with modern web technologies, secure authentication, and powerful automation capabilities.*