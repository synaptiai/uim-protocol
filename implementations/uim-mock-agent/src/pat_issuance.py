from typing import Dict, Any
from cryptography.hazmat.primitives import serialization
import requests
import base64
from error_handling import NetworkError
from key_management import get_key_pair

def handle_pat_issuance(signed_policy: str, agent_id: str) -> Dict:
    private_key, public_key = get_key_pair("http://localhost:4000")
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    public_key_base64url = base64.urlsafe_b64encode(public_key_pem).decode('utf-8')
    
    payload = { "signed_policy": signed_policy, "agent_id": agent_id, "agent_public_key": public_key_base64url}
    headers = {
        "Content-Type": "application/json"
    }
    try:
        print(f"Submitting signed policy for verification and PAT issuance: {payload}")
        response = requests.post("http://localhost:4000/pat/issue", json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise NetworkError(f"Error executing intent: {str(e)}")
