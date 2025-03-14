import requests
from typing import Dict, Any
from error_handling import NetworkError, APIError

MOCK_SERVICE_URL = "http://localhost:4000"

def execute_intent(intent_uid: str, params: Dict[str, Any], execute_endpoint: str, pat: str) -> Dict[str, Any]:
    """
    Execute an intent with the given parameters and PAT.

    Args:
        intent_uid (str): The UID of the intent to execute.
        params (Dict[str, Any]): The parameters for the intent.
        execute_endpoint (str): The endpoint for executing the intent.
        pat (str): Personal Access Token for authentication.

    Returns:
        Dict[str, Any]: The result of the intent execution.
    """
    print(f"Debug: Intent UID: {intent_uid}")
    print(f"Debug: Parameters: {params}")
    print(f"Debug: Execute Endpoint: {execute_endpoint}")

    url = execute_endpoint
    print(f"Debug: Constructed URL: {url}")

    payload = {
        "intent_uid": intent_uid,
        "parameters": params
    }
    print(f"Debug: Payload: {payload}")

    headers = {
        "Authorization": f"Bearer {pat}",
        "Content-Type": "application/json"
    }
    print(f"Debug: Headers: {headers}")

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise NetworkError(f"Error executing intent: {str(e)}")

def get_intent_params(intent_uid: str) -> Dict[str, Any]:
    """
    Get the required parameters for an intent.

    Args:
        intent_uid (str): The UID of the intent.

    Returns:
        Dict[str, Any]: The required parameters for the intent.
    """
    url = f"{MOCK_SERVICE_URL}/agents.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        agents_data = response.json()
        for intent in agents_data.get("intents", []):
            if intent.get("intent_uid") == intent_uid:
                return intent.get("input_parameters", {})
        return {}
    except requests.RequestException as e:
        raise NetworkError(f"Error fetching intent parameters: {str(e)}")
    except ValueError as e:
        raise APIError(f"Error parsing intent parameters: {str(e)}")