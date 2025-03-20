"""Configuration File"""

import os 
from dotenv import load_dotenv

# Load environment variables from .env file 
load_dotenv()

# API Configuration
BASE_URL = os.getenv("HALO_BASE_URL", "https://crm.hivedome.net")
API_BASE_URL = os.getenv("HALO_API_BASE_URL", "https://crm.hivedome.net/api")
AUTH_ENDPOINT = os.getenv("HALO_AUTH_ENDPOINT", "/auth/token")
KB_ENDPOINT = os.getenv("HALO_KB_ENDPOINT", "/KBArticle")

# Authentication 
CLIENT_ID = os.getenv("CLIENT_ID")
USERNAME = os.getenv("HALO_USERNAME")
PASSWORD = os.getenv("HALO_PASSWORD") 

# Output Configuration 
OUTPUT_DIR = os.getenv("OUTPUT_DIR")

# Request Settings
REQUEST_TIMEOUT = os.getenv("REQUEST_TIME_OUT")