"""Exceptions"""

class HaloApiError(Exception):
    """Base exception for Halo API errors"""
    pass 

class AuthenticationError(HaloApiError):
    """Raised when authentication fails"""
    pass 
    
    
class ArticleNotFoundError(HaloApiError):
    """Raised when an article is not found"""
    pass

class ApiRequestError(HaloApiError):
    """Raised when an API request fails"""
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(f"API request failed with status {status_code}: {message}")