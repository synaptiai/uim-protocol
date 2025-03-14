from intent_execution import execute_intent, get_intent_params
from error_handling import handle_error, UIMMockAgentError
from discovery import fetch_agents_json, extract_intent_metadata
from policy_management import fetch_policy, display_policy
from policy_signing import sign_policy
from pat_issuance import handle_pat_issuance
from key_management import generate_key_pair, get_key_pair
import json
import os

current_pat = None
current_service_url = None

def display_menu():
    print("\nUIM Mock Agent CLI")
    print("1. Manage Keys")
    print("2. Discover Intents")
    print("3. View Policy")
    print("4. Sign Policy and Get PAT")
    print("5. Execute Intent")
    print("6. Exit")

def get_user_choice():
    try:
        choice = input("Enter your choice (1-7): ")
        return choice
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def handle_discover_intents():
    global current_service_url
    try:
        agents_json = fetch_agents_json()
        current_service_url = agents_json.get("service_url", "http://localhost:4000")
        metadata = extract_intent_metadata(agents_json)
        intents = metadata["intents"]
        print("\nAvailable Intents:")
        for intent in intents:
            print(f"- {intent['name']}: {intent['description']} (Agent: {intent['agent']})")
    except Exception as e:
        print(handle_error(e))

def handle_execute_intent():
    global current_pat
    if not current_pat:
        print("No PAT available. Please sign the policy and get a PAT first.")
        return

    try:
        intent_uid = input("Enter the intent UID: ")
        params = get_intent_params(intent_uid)
        user_params = {}
        for param, details in params.items():
            user_params[param] = input(f"Enter value for {param} ({details['type']}): ")

        agents_json = fetch_agents_json()
        execute_endpoint = agents_json.get("uim-api-execute", "http://localhost:4000/uim/execute")

        result = execute_intent(intent_uid, user_params, execute_endpoint, current_pat)
        print("Intent Execution Result:")
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error executing intent: {str(e)}")

def handle_view_policy():
    try:
        policy = fetch_policy()
        display_policy(policy)
    except Exception as e:
        print(handle_error(e))

def handle_sign_policy_and_get_pat():
    global current_pat
    global current_service_url
    try:
        policy = fetch_policy()
        signed_policy = sign_policy(policy, current_service_url)
        agent_id = input("Enter your agent ID: ")
        result = handle_pat_issuance(signed_policy, agent_id)
        if result["uim-pat"]:
            current_pat = result["uim-pat"]
            print(f"PAT issued successfully: {current_pat}")
        else:
            print(f"Failed to issue PAT: {result['error']}")
    except Exception as e:
        print(handle_error(e))

def handle_key_management():
    global current_service_url
    print("\nKey Management")
    print("1. Generate new key pair")
    print("2. View existing key pair")
    print("3. Set current service URL")
    choice = input("Enter your choice (1-3): ")

    try:
        if choice == '1':
            if not current_service_url:
                print("Please set the current service URL first.")
                return
            generate_key_pair(current_service_url)
            print(f"New key pair generated for {current_service_url}")
        elif choice == '2':
            if not current_service_url:
                print("Please set the current service URL first.")
                return
            private_key, public_key = get_key_pair(current_service_url)
            print(f"Existing key pair for {current_service_url}:")
            print(f"Private key: {private_key}")
            print(f"Public key: {public_key}")
        elif choice == '3':
            current_service_url = input("Enter the service URL: ")
            print(f"Current service URL set to: {current_service_url}")
        else:
            print("Invalid choice")
    except Exception as e:
        print(handle_error(e))

def main():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            handle_key_management()            
        elif choice == '2':
            handle_discover_intents()
        elif choice == '3':
            handle_view_policy()
        elif choice == '4':
            handle_sign_policy_and_get_pat()
        elif choice == '5':
            handle_execute_intent()
        elif choice == '6':
            print("Exiting UIM Mock Agent CLI. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
