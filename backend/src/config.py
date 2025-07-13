import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("KISS_MYSQL_HOST", "localhost")
DB_USER = os.getenv("KISS_MYSQL_USER", "kiss_user")
DB_PASSWORD = os.getenv("KISS_MYSQL_PASSWORD", "kiss_password")
DB_NAME = os.getenv("KISS_MYSQL_DATABASE", "kiss_game")
DB_PORT = int(os.getenv("KISS_MYSQL_PORT", "3306"))

# Application configuration
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-this")

# Server configuration
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))
