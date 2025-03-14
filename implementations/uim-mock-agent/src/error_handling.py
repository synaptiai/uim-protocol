import requests

class UIMMockAgentError(Exception):
    """Base exception class for UIM Mock Agent"""
    pass

class NetworkError(UIMMockAgentError):
    """Exception raised for network-related errors"""
    pass

class APIError(UIMMockAgentError):
    """Exception raised for API-related errors"""
    pass

class InputError(UIMMockAgentError):
    """Exception raised for invalid input errors"""
    pass

def handle_http_error(e: requests.RequestException) -> str:
    """Handle HTTP errors and return user-friendly error messages"""
    status_code = e.response.status_code if e.response else None
    if status_code == 400:
        return "Bad request. Please check your input and try again."
    elif status_code == 401:
        return "Unauthorized. Please check your credentials and try again."
    elif status_code == 403:
        return "Forbidden. You don't have permission to access this resource."
    elif status_code == 404:
        return "Resource not found. Please check the URL and try again."
    elif status_code == 429:
        return "Too many requests. Please wait and try again later."
    elif status_code == 500:
        return "Internal server error. Please try again later or contact support."
    elif status_code == 503:
        return "Service unavailable. Please try again later."
    else:
        return f"An error occurred: {str(e)}"

def handle_error(e: Exception) -> str:
    """Handle various types of errors and return user-friendly error messages"""
    if isinstance(e, requests.RequestException):
        return handle_http_error(e)
    elif isinstance(e, NetworkError):
        return "A network error occurred. Please check your internet connection and try again."
    elif isinstance(e, APIError):
        return "An API error occurred. Please try again later or contact support."
    elif isinstance(e, InputError):
        return f"Invalid input: {str(e)}"
    else:
        return f"An unexpected error occurred: {str(e)}"