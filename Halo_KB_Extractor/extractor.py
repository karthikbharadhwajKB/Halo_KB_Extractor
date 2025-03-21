import os 
import json 
from typing import Dict, List, Union, Any 

from client import HaloClient
from config import OUTPUT_DIR

class KBExtractor:
    def __init__(self):
        self.client = HaloClient()
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
    def extract_article(self, article_id: int) -> None: 
        article = self.client.get_article(article_id)
        self._save_article(article)
        
    def extract_articles(self, article_ids: List[int]) -> None:
        articles = self.client.get_articles(article_ids)
        for article in articles:
            self._save_article(article)
            
    def _save_article(self, article: Dict[str, Any]) -> None: 
        article_id = article.get("id")
        article_name = article.get("name", "Unnamed Article")
        filename = f"{article_id}_{self._sanitize_filename(article_name)}.txt"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        extracted_data = {
            "name": article.get("name", ""),
            "description": article.get("description", ""),
            "resolution": article.get("resolution", "")
        }
        
        with open(filepath, "w", encoding="utf-8") as f: 
            f.write(extracted_data['name'] + "\n\n")
            if extracted_data['description']:
                f.write(extracted_data["description"])
            if extracted_data['resolution']:
                f.write(extracted_data["resolution"])
        
    def _sanitize_filename(self, filename: str) -> str:
        invalid_chars = '<>:"/\\|?*' 
        for char in invalid_chars:
            filename = filename.replace(char, "_")
        return filename[:50]