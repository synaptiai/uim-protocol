"""
PAT Issuance module for UIM Mock Agent.

This module provides functionality for obtaining Policy Adherence Tokens (PATs)
from UIM-compatible web services by submitting signed policies.
"""
import base64
from typing import Dict

import requests
from cryptography.hazmat.primitives import serialization
from error_handling import NetworkError
from key_management import get_key_pair


def handle_pat_issuance(signed_policy: str, agent_id: str) -> Dict:
    """
    Handle the issuance of a Policy Adherence Token (PAT).

    This function submits a signed policy to the UIM service along with the agent's
    public key to obtain a PAT that can be used for subsequent intent executions.

    Args:
        signed_policy: The JWT-encoded signed policy
        agent_id: The unique identifier for the agent

    Returns:
        Dict: The response from the PAT issuance endpoint, containing the PAT

    Raises:
        NetworkError: If there's an issue with the network request
    """
    private_key, public_key = get_key_pair("http://localhost:4000")
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    public_key_base64url = base64.urlsafe_b64encode(public_key_pem).decode("utf-8")

    payload = {
        "signed_policy": signed_policy,
        "agent_id": agent_id,
        "agent_public_key": public_key_base64url,
    }
    headers = {"Content-Type": "application/json"}

    try:
        print(f"Submitting signed policy for verification and PAT issuance: {payload}")
        response = requests.post(
            "http://localhost:4000/pat/issue", json=payload, headers=headers
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise NetworkError(f"Error executing intent: {str(e)}")
