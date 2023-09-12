import os


# Common configuration options
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")

def get_config():
    # Additional configuration options for testing
    
    if os.getenv("FLASK_ENV")=='testing':
        return 'mysql://'+os.getenv("DB_USERNAME")+":"+os.getenv("DB_PASSWORD") +'@'+os.getenv("DB_HOST")+':'+os.getenv("DB_PORT")+'/'+os.getenv("DB_NAME_TESTING")
    else:
         return 'mysql://'+os.getenv("DB_USERNAME")+":"+os.getenv("DB_PASSWORD") +'@'+os.getenv("DB_HOST")+':'+os.getenv("DB_PORT")+'/'+os.getenv("DB_NAME")
