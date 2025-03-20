import requests 
from typing import Dict, List, Optional, Any 

from auth import HaloAuth
from config import API_BASE_URL, KB_ENDPOINT

class HaloClient:
    def __init__(self):
        self.auth = HaloAuth()
        self.base_api_url = API_BASE_URL
        self.kb_endpoint = KB_ENDPOINT
    
    def get_article(self, article_id: int) -> Dict[str, Any]:
        endpoint = f"{self.kb_endpoint}{article_id}" 
        return self._make_api_request("GET", endpoint)
    
    def get_articles(self, article_ids: List[int]) -> List[Dict[str, Any]]: 
        articles = []
        for article_id in article_ids:
            try: 
                article = self.get_article(article_id)
                articles.append(article)
            except Exception as e: 
                print(f"Something went wrong: {str(e)}")
        return articles
    
    
    def _make_api_request(self, 
                          method: str, 
                          endpoint: str, 
                          params: Optional[Dict] = None,
                          data: Optional[Dict] = None,) -> Any:
        # Header
        headers = self.auth.get_auth_headers()
        # base url 
        url = f"{self.base_api_url}{endpoint}"
        try: 
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=data
            )
            if response.status_code >= 400: 
                error_message = response.text
                try: 
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        error_message = error_data.get("message", error_message)
                except: 
                    pass
                raise Exception(f"API request failed with status {response.status_code}: {error_message}")
            return response.json()
        except requests.RequestException as e: 
            raise Exception(f"Request failed: {str(e)}")