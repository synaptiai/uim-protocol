"""
Discovery module for UIM Mock Agent.

This module provides functionality for discovering UIM services and their intents
by fetching and parsing agents.json files from UIM-compatible web services.
"""
import json
from typing import Dict

import requests
from error_handling import APIError, NetworkError, handle_error
from key_management import get_key_pair

SERVICE_URL = "http://localhost:4000"  # Adjust this URL if needed
AGENTS_ENDPOINT = f"{SERVICE_URL}/agents.json"


def fetch_agents_json() -> Dict:
    """
    Fetch the agents.json file from the UIM service.

    Returns:
        Dict: The parsed JSON content of the agents.json file

    Raises:
        NetworkError: If there's an issue with the network request
        APIError: If there's an issue parsing the JSON response
    """
    try:
        response = requests.get(AGENTS_ENDPOINT)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise NetworkError(f"Error fetching agents.json: {str(e)}")
    except json.JSONDecodeError as e:
        raise APIError(f"Error parsing agents.json: {str(e)}")


def extract_intent_metadata(agents_data: Dict) -> Dict:
    """
    Extract intent metadata from the agents.json data.

    Args:
        agents_data: The parsed agents.json data

    Returns:
        Dict: A dictionary containing extracted intents, execute endpoint, and service URL
    """
    print(f"Debug: agents_data structure: {json.dumps(agents_data, indent=2)}")
    intents = []
    execute_endpoint = agents_data.get("uim-api-execute")
    print(f"Debug: execute_endpoint: {execute_endpoint}")

    service_url = agents_data.get("service-info", {}).get("service_url", SERVICE_URL)

    for intent in agents_data.get("intents", []):
        print(f"Debug: Processing intent: {json.dumps(intent, indent=2)}")
        intents.append(
            {
                "name": intent.get("intent_name"),
                "description": intent.get("description"),
                "agent": agents_data.get("service-info", {}).get("name"),
                "intent_uid": intent.get("intent_uid"),
                "service_url": service_url,
            }
        )

    print(f"Debug: Extracted intents: {json.dumps(intents, indent=2)}")
    return {
        "intents": intents,
        "execute_endpoint": execute_endpoint,
        "service_url": service_url,
    }


def main():
    """
    Main function for testing the discovery module functionality.

    Fetches agents.json, extracts intent metadata, and displays the results.
    """
    try:
        agents_data = fetch_agents_json()
        print(f"Debug: Full agents_data structure: {json.dumps(agents_data, indent=2)}")
        service_info = agents_data.get("service-info", {})
        print(f"Debug: service_info: {service_info}")

        metadata = extract_intent_metadata(agents_data)
        print(f"Debug: metadata: {metadata}")

        intent_metadata = metadata["intents"]
        print(f"Debug: intent_metadata: {intent_metadata}")

        service_url = metadata["service_url"]
        private_key, public_key = get_key_pair(service_url)

        print(f"Service: {service_info.get('name')}")
        print(f"Description: {service_info.get('description')}")
        print(f"Service URL: {service_url}")
        print("\nAvailable Intents:")
        for intent in intent_metadata:
            print(f"Debug: Processing intent: {intent}")
            print(f"- {intent['name']} ({intent['agent']}): {intent['description']}")

        print(f"\nKey pair retrieved for service URL: {service_url}")

    except Exception as e:
        print(f"Debug: Exception occurred: {str(e)}")
        print(f"Debug: Exception type: {type(e)}")
        print(handle_error(e))


if __name__ == "__main__":
    main()
