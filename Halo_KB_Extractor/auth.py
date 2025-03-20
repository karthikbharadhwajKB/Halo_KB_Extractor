import requests
import time
from typing import Dict

from config import BASE_URL, AUTH_ENDPOINT, USERNAME, PASSWORD, CLIENT_ID

class HaloAuth:
    def __init__(self): 
        self.access_token = None 
        self.token_expiry = 0  
        # authenticate
        self.client_id = CLIENT_ID
        self.username = USERNAME
        self.password = PASSWORD
        # Auth endpoint
        self.api_base_url = BASE_URL
        self.auth_endpoint = AUTH_ENDPOINT
        
        
    def get_auth_headers(self) -> Dict[str,str]:
        if not self.access_token:
            self._authenticate()
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        } 
        
    def is_token_valid(self) -> bool:
        return self.access_token is not None and time.time() < self.token_expiry

    def _authenticate(self) -> None: 
        auth_data = {
            "grant_type": "password",
            "client_id": self.client_id, 
            "username": self.username,
            "password": self.password,
            "scope": "all"
        }
        try: 
            response = requests.post(
                f"{self.api_base_url}{self.auth_endpoint}", 
                data=auth_data
            )
            if response.status_code != 200: 
                raise Exception(f"Authentication failed with status code {response.status_code}")
            auth_response = response.json()
            self.access_token = auth_response.get("access_token")
        except requests.RequestException as re:
            raise Exception(f"Authentication request failed: {str(re)}")
            