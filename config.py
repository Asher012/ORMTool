# ReviewForge Analytics Pro Enhanced - Configuration File
# config.py

import os
from datetime import timedelta

class Config:
    """Configuration settings for ReviewForge Analytics Pro Enhanced"""
    
    # Application Settings
    APP_NAME = "ReviewForge Analytics Pro Enhanced"
    VERSION = "3.0.0"
    DEVELOPER = "Ayush Pandey"
    
    # Security Settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-super-secret-key-change-this-in-production'
    SESSION_TIMEOUT = timedelta(hours=24)  # User session timeout
    MAX_LOGIN_ATTEMPTS = 5
    PASSWORD_MIN_LENGTH = 6
    
    # Database Settings
    DATABASE_PATH = 'reviewforge_users.db'
    BACKUP_DATABASE = True
    
    # Analysis Settings
    DEFAULT_REVIEW_COUNT = 500
    MAX_REVIEW_COUNT = 2000
    DEFAULT_SENTIMENT_THRESHOLD = 0.6
    ENABLE_ASPECT_ANALYSIS = True
    ENABLE_EMOTION_DETECTION = True
    ENABLE_TOPIC_MODELING = True
    DEFAULT_TOPIC_COUNT = 5
    
    # GMB Scraping Settings
    GMB_DEFAULT_MAX_REVIEWS = 100
    GMB_TIMEOUT_SECONDS = 30
    GMB_SCROLL_PAUSE_TIME = 1.0
    GMB_USE_HEADLESS = True
    
    # Automation Settings
    DEFAULT_MONITORING_INTERVAL = 30  # minutes
    MIN_MONITORING_INTERVAL = 15     # minutes
    MAX_MONITORING_INTERVAL = 1440   # 24 hours
    AUTO_START_SCHEDULER = False
    
    # Webhook Settings
    WEBHOOK_TIMEOUT = 10  # seconds
    MAX_WEBHOOK_RETRIES = 3
    NOTIFICATION_RATE_LIMIT = 60  # seconds between notifications
    
    # Google Sheets Settings
    SHEETS_DEFAULT_SPREADSHEET = "ReviewForge_Analytics"
    SHEETS_DEFAULT_WORKSHEET = "Reviews"
    SHEETS_AUTO_CREATE = True
    
    # Export Settings
    EXPORT_DATE_FORMAT = "%Y%m%d_%H%M%S"
    MAX_EXPORT_ROWS = 10000
    EXPORT_FORMATS = ['csv', 'xlsx', 'json']
    
    # UI Settings
    PAGE_TITLE = "ReviewForge Analytics Pro Enhanced"
    PAGE_ICON = "📊"
    LAYOUT = "wide"
    SIDEBAR_STATE = "expanded"
    
    # Performance Settings
    CACHE_TTL = 3600  # 1 hour
    MAX_CONCURRENT_REQUESTS = 5
    REQUEST_DELAY = 1.0  # seconds between requests
    
    # Logging Settings
    LOG_LEVEL = "INFO"
    LOG_FILE = "reviewforge.log"
    LOG_MAX_SIZE = 10 * 1024 * 1024  # 10MB
    LOG_BACKUP_COUNT = 5
    
    # Rate Limiting
    API_RATE_LIMIT = 100  # requests per hour
    SCRAPING_RATE_LIMIT = 10  # requests per minute
    
    # File Upload Settings
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS = ['.json', '.csv', '.xlsx']
    UPLOAD_FOLDER = 'uploads'
    
    # Notification Messages
    MESSAGES = {
        'login_success': "Welcome back! Login successful.",
        'login_failed': "Invalid credentials. Please try again.",
        'analysis_complete': "Analysis completed successfully!",
        'export_success': "Data exported successfully!",
        'webhook_test': "Test notification from ReviewForge Analytics",
        'automation_started': "Automated monitoring has been started",
        'automation_stopped': "Automated monitoring has been stopped",
        'negative_review_alert': "New negative review detected",
        'system_error': "System error occurred. Please try again."
    }
    
    # Color Theme
    COLORS = {
        'primary': '#667eea',
        'primary_dark': '#5a67d8',
        'secondary': '#764ba2',
        'accent': '#f093fb',
        'success': '#48bb78',
        'warning': '#ed8936',
        'error': '#f56565',
        'info': '#4299e1',
        'dark': '#1a202c',
        'light': '#f7fafc'
    }
    
    # Feature Flags
    FEATURES = {
        'gmb_analysis': True,
        'automation': True,
        'webhooks': True,
        'google_sheets': True,
        'user_management': True,
        'export_advanced': True,
        'competitor_analysis': True,
        'trend_analysis': True,
        'deep_learning': True,
        'multi_language': False,  # Future feature
        'real_time_monitoring': True
    }

# Development Configuration
class DevelopmentConfig(Config):
    DEBUG = True
    GMB_USE_HEADLESS = False  # Show browser in development
    LOG_LEVEL = "DEBUG"
    AUTO_START_SCHEDULER = False

# Production Configuration  
class ProductionConfig(Config):
    DEBUG = False
    GMB_USE_HEADLESS = True
    LOG_LEVEL = "WARNING"
    AUTO_START_SCHEDULER = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-must-set-a-secret-key-in-production'

# Testing Configuration
class TestingConfig(Config):
    TESTING = True
    DATABASE_PATH = ':memory:'  # In-memory database for testing
    GMB_DEFAULT_MAX_REVIEWS = 10
    DEFAULT_REVIEW_COUNT = 50

# Configuration selector
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}