import jwt
from typing import Dict
from error_handling import APIError
from cryptography.hazmat.primitives import serialization
from pat_issuance import handle_pat_issuance
from key_management import get_key_pair

MOCK_SERVICE_URL = "http://localhost:4000"
POLICY_VERIFICATION_ENDPOINT = f"{MOCK_SERVICE_URL}/pat/issue"

def sign_policy(policy: Dict, service_url: str) -> str:
    """
    Sign the policy using the AI agent's private key.

    Args:
        policy (Dict): The policy to be signed
        service_url (str): The URL of the service to get the key pair for

    Returns:
        str: The signed policy as a JWS token
    """
    try:
        private_key, _ = get_key_pair(service_url)
        jws_token = jwt.encode(policy, private_key, algorithm="RS256")
        return jws_token
    except Exception as e:
        raise APIError(f"Error signing policy: {str(e)}")

def submit_signed_policy_and_get_pat(signed_policy: str, service_url: str) -> Dict:
    """
    Submit the signed policy for verification and PAT issuance.

    Args:
        signed_policy (str): The signed policy as a JWS token
        service_url (str): The URL of the service to get the key pair for

    Returns:
        Dict: The response containing the PAT
    """
    try:
        agent_id = "ai-agent-1"  # This should be a unique identifier for your AI agent
        _, public_key = get_key_pair(service_url)
        public_key_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')

        result = handle_pat_issuance(signed_policy, agent_id, public_key_pem)

        if result["success"]:
            return {"pat": result["pat"]}
        else:
            raise APIError(f"Error issuing PAT: {result['error']}")
    except Exception as e:
        raise APIError(f"Error in PAT issuance process: {str(e)}")