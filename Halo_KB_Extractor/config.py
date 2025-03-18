"""Configuration File"""

import os 
from dotenv import load_dotenv

# Load environment variables from .env file 
load_dotenv()

# API Configuration
API_BASE_URL = os.getenv("HALO_API_BASE_URL")
AUTH_ENDPOINT = os.getenv("HALO_AUTH_ENDPOINT")
KB_ENDPOINT = os.getenv("HALO_KB_ENDPOINT")

# Authentication 
USERNAME = os.getenv("HALO_USER_NAME")
PASSWORD = os.getenv("HALO_PASSWORD") 

# Output Configuration 
OUTPUT_DIR = os.getenv("OUTPUT_DIR")

# Request Settings
REQUEST_TIMEOUT = os.getenv("REQUEST_TIME_OUT")