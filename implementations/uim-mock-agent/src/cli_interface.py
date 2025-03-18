"""
Command-line interface for the UIM Mock Agent.

This module provides a CLI for interacting with UIM services, including
discovering intents, managing keys, viewing policies, and executing intents.
"""

import json

from discovery import extract_intent_metadata, fetch_agents_json
from error_handling import handle_error
from intent_execution import execute_intent, get_intent_params
from key_management import generate_key_pair, get_key_pair
from pat_issuance import handle_pat_issuance
from policy_management import display_policy, fetch_policy
from policy_signing import sign_policy

# Module-level variables
CURRENT_PAT = None
CURRENT_SERVICE_URL = None


def display_menu():
    """Display the main menu options for the UIM Mock Agent CLI."""
    print("\nUIM Mock Agent CLI")
    print("1. Manage Keys")
    print("2. Discover Intents")
    print("3. View Policy")
    print("4. Sign Policy and Get PAT")
    print("5. Execute Intent")
    print("6. Exit")


def get_user_choice():
    """
    Get the user's menu choice.

    Returns:
        str or None: The user's choice as a string, or None if input is invalid.
    """
    try:
        choice = input("Enter your choice (1-7): ")
        return choice
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def handle_discover_intents():
    """
    Discover and display available intents from the UIM service.

    Updates the CURRENT_SERVICE_URL global variable with the service URL
    from the agents.json file.
    """
    global CURRENT_SERVICE_URL
    try:
        agents_json = fetch_agents_json()
        CURRENT_SERVICE_URL = agents_json.get("service_url", "http://localhost:4000")
        metadata = extract_intent_metadata(agents_json)
        intents = metadata["intents"]
        print("\nAvailable Intents:")
        for intent in intents:
            print(
                f"- {intent['name']}: {intent['description']} "
                f"(Agent: {intent['agent']})"
            )
    except Exception as e:
        print(handle_error(e))


def handle_execute_intent():
    """
    Execute an intent with user-provided parameters.

    Requires a valid PAT (Policy Adherence Token) to be set.
    Prompts the user for the intent UID and parameter values.
    """
    global CURRENT_PAT
    if not CURRENT_PAT:
        print("No PAT available. Please sign the policy and get a PAT first.")
        return

    try:
        intent_uid = input("Enter the intent UID: ")
        params = get_intent_params(intent_uid)
        user_params = {}
        for param, details in params.items():
            user_params[param] = input(f"Enter value for {param} ({details['type']}): ")

        agents_json = fetch_agents_json()
        execute_endpoint = agents_json.get(
            "uim-api-execute", "http://localhost:4000/uim/execute"
        )

        result = execute_intent(intent_uid, user_params, execute_endpoint, CURRENT_PAT)
        print("Intent Execution Result:")
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error executing intent: {str(e)}")


def handle_view_policy():
    """
    Fetch and display the service policy.

    Retrieves the policy from the service and displays it to the user.
    """
    try:
        policy = fetch_policy()
        display_policy(policy)
    except Exception as e:
        print(handle_error(e))


def handle_sign_policy_and_get_pat():
    """
    Sign the service policy and obtain a Policy Adherence Token (PAT).

    Fetches the policy, signs it, and requests a PAT from the service.
    Updates the CURRENT_PAT global variable with the obtained token.
    """
    global CURRENT_PAT
    global CURRENT_SERVICE_URL
    try:
        policy = fetch_policy()
        signed_policy = sign_policy(policy, CURRENT_SERVICE_URL)
        agent_id = input("Enter your agent ID: ")
        result = handle_pat_issuance(signed_policy, agent_id)
        if result["uim-pat"]:
            CURRENT_PAT = result["uim-pat"]
            print(f"PAT issued successfully: {CURRENT_PAT}")
        else:
            print(f"Failed to issue PAT: {result['error']}")
    except Exception as e:
        print(handle_error(e))


def handle_key_management():
    """
    Handle key management operations.

    Provides a submenu for key management operations:
    1. Generate a new key pair for the current service URL
    2. View the existing key pair for the current service URL
    3. Set the current service URL
    """
    global CURRENT_SERVICE_URL
    print("\nKey Management")
    print("1. Generate new key pair")
    print("2. View existing key pair")
    print("3. Set current service URL")
    choice = input("Enter your choice (1-3): ")

    try:
        if choice == "1":
            if not CURRENT_SERVICE_URL:
                print("Please set the current service URL first.")
                return
            generate_key_pair(CURRENT_SERVICE_URL)
            print(f"New key pair generated for {CURRENT_SERVICE_URL}")
        elif choice == "2":
            if not CURRENT_SERVICE_URL:
                print("Please set the current service URL first.")
                return
            private_key, public_key = get_key_pair(CURRENT_SERVICE_URL)
            print(f"Existing key pair for {CURRENT_SERVICE_URL}:")
            print(f"Private key: {private_key}")
            print(f"Public key: {public_key}")
        elif choice == "3":
            CURRENT_SERVICE_URL = input("Enter the service URL: ")
            print(f"Current service URL set to: {CURRENT_SERVICE_URL}")
        else:
            print("Invalid choice")
    except Exception as e:
        print(handle_error(e))


def main():
    """
    Main entry point for the UIM Mock Agent CLI.

    Displays the menu and handles user choices in a loop until the user chooses to exit.
    """
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == "1":
            handle_key_management()
        elif choice == "2":
            handle_discover_intents()
        elif choice == "3":
            handle_view_policy()
        elif choice == "4":
            handle_sign_policy_and_get_pat()
        elif choice == "5":
            handle_execute_intent()
        elif choice == "6":
            print("Exiting UIM Mock Agent CLI. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
