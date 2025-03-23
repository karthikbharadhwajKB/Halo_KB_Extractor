import argparse
import sys
from typing import List, Union

from extractor import KBExtractor

def parse_article_ids(ids_str: str) -> List[int]:
    try: 
        return [int(id_str.strip()) for id_str in ids_str.split(",") if id_str.strip()]
    except ValueError: 
        raise ValueError("Articles IDs must be integers")

def main(): 
    parser = argparse.ArgumentParser(description="Extract Knowledge Base articles from Halo PSA")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--id", "-i", help="Single article ID to extract")
    group.add_argument("--ids", "-l", help="Comma-separated list of article IDs to extract")
    args = parser.parse_args()
    
    try: 
        extractor = KBExtractor()
        if args.id: 
            try :
                article_id = int(args.id)
                extractor.extract_article(article_id)
            except ValueError:
                print("Error: Article IDs must be an Integer", file=sys.stderr)
                sys.exit(1)
        elif args.ids: 
            try: 
                article_ids = parse_article_ids(args.ids)
                extractor.extract_articles(article_ids)
            except ValueError as ve: 
                print(f"Error: {str(ve)}", file=sys.stderr)
                sys.exit(1)
    except Exception as e: 
        print(f"Unexpected error: {str(e)}", file=sys.stderr)
        sys.exit(1)
        
    
if __name__ == "__main__": 
    main()
        
                