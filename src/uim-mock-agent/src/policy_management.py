import requests
from error_handling import NetworkError, APIError
from policy_signing import sign_policy, submit_signed_policy_and_get_pat

MOCK_SERVICE_URL = "http://localhost:4000"
POLICY_ENDPOINT = f"{MOCK_SERVICE_URL}/uim-policy.json"

def fetch_policy():
    try:
        response = requests.get(POLICY_ENDPOINT)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise NetworkError(f"Error fetching policy: {str(e)}")
    except ValueError as e:
        raise APIError(f"Error parsing policy JSON: {str(e)}")

def display_policy(policy):
    print("\nODRL Policy:")
    print(f"Context: {policy.get('@context')}")
    print(f"Type: {policy.get('@type')}")
    print(f"ID: {policy.get('@id')}")
    print(f"Profile: {policy.get('profile')}")

    print("\nPermissions:")
    for permission in policy.get('permission', []):
        print(f"- Target: {permission.get('target')}")
        print(f"  Action: {permission.get('action', {}).get('id')}")
        for refinement in permission.get('action', {}).get('refinement', []):
            print(f"    Refinement: {refinement.get('leftOperand')} {refinement.get('operator')} {refinement.get('rightOperand')} {refinement.get('unit')}")

    print("\nProhibitions:")
    for prohibition in policy.get('prohibition', []):
        print(f"- Targets: {', '.join(prohibition.get('target', []))}")
        print(f"  Action: {prohibition.get('action', {}).get('id')}")
        for refinement in prohibition.get('action', {}).get('refinement', []):
            print(f"    Refinement: {refinement.get('leftOperand')} {refinement.get('operator')} {refinement.get('rightOperand')} {refinement.get('unit')}")

    print("\nParties:")
    for party in policy.get('party', []):
        print(f"- Function: {party.get('function')}")
        print(f"  Identifier: {party.get('identifier')}")

    print("\nAssets:")
    for asset in policy.get('asset', []):
        print(f"- ID: {asset.get('id')}")
        print(f"  Type: {asset.get('type')}")

def process_policy():
    try:
        policy = fetch_policy()
        display_policy(policy)

        signed_policy = sign_policy(policy)
        print(f"\nSigned Policy: {signed_policy}")

        pat_result = submit_signed_policy_and_get_pat(signed_policy)
        if "pat" in pat_result:
            print(f"\nPAT Issuance Result: Success")
            print(f"Personal Access Token: {pat_result['pat']}")
        else:
            print(f"\nPAT Issuance Result: Failed")
            print(f"Error: {pat_result.get('error', 'Unknown error')}")

        return pat_result
    except (NetworkError, APIError) as e:
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    process_policy()