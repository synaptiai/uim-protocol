"""
UIM Mock Webservice.

This module implements a mock webservice for the UIM protocol, providing endpoints
for policy retrieval, PAT issuance, and intent execution. It simulates a real estate
service with search and property details intents.
"""

import base64
import os
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any, Dict

import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()


class SearchRequest(BaseModel):
    """Request model for property search intent."""

    location: str
    min_price: int = None
    max_price: int = None
    property_type: str = None


class SearchResponse(BaseModel):
    """Response model for property search intent."""

    properties: list
    total_results: int


class DetailsRequest(BaseModel):
    """Request model for property details intent."""

    property_id: str


class DetailsResponse(BaseModel):
    """Response model for property details intent."""

    property_details: dict


class PolicyAgreementRequest(BaseModel):
    """Request model for policy agreement and PAT issuance."""

    agent_id: str = Field(..., description="The unique identifier of the agent")
    signed_policy: str = Field(
        ..., min_length=1, description="The signed policy document"
    )
    agent_public_key: str = Field(
        ..., min_length=1, description="The public key of the agent"
    )


class ExecuteRequest(BaseModel):
    """Request model for intent execution."""

    intent_uid: str = Field(..., description="The unique identifier of the intent")
    parameters: Dict[str, Any] = Field(..., description="The parameters for the intent")


app = FastAPI()


def get_key_pair(as_string: bool = False):
    """
    Get the key pair for the service.

    """
    try:
        private_key_path = os.path.join("keys", "private_key.pem")
        public_key_path = os.path.join("keys", "public_key.pem")

        if not os.path.exists(private_key_path) or not os.path.exists(public_key_path):
            print("Key pair not found for service under /keys.")
            raise FileNotFoundError("Key pair not found.")

        with open(private_key_path, "rb") as f:
            if as_string:
                private_key = f.read().decode("utf-8")
            else:
                private_key = serialization.load_pem_private_key(
                    f.read(), password=None, backend=default_backend()
                )

        with open(public_key_path, "rb") as f:
            if as_string:
                public_key = f.read().decode("utf-8")
            else:
                public_key = serialization.load_pem_public_key(
                    f.read(), backend=default_backend()
                )

        print("Key pair loaded for service under /keys.")
        return private_key, public_key
    except Exception as e:
        print(f"Error loading key pair for service: {e}")
        raise


UIM_SERVICE_PRIVATE_KEY, UIM_SERVICE_PUBLIC_KEY = get_key_pair()
UIM_SERVICE_LICENSE = os.getenv("UIM_SERVICE_LICENSE")


@app.get("/agents.json")
async def get_agents_json(request: Request):
    """
    Endpoint to retrieve the agents.json file.

    This endpoint provides information about the service, available intents,
    and UIM-specific configuration.

    Args:
        request: The FastAPI request object

    Returns:
        JSONResponse: The agents.json content
    """
    agents_json = create_agents_json(request)
    return JSONResponse(content=agents_json)


def create_agents_json(request: Request):
    """
    Create the agents.json content.

    Args:
        request: The FastAPI request object

    Returns:
        dict: The agents.json content
    """
    base_url = f"{request.url.scheme}://{request.client.host}:{request.url.port}"
    public_key_pem = UIM_SERVICE_PUBLIC_KEY.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    public_key_base64url = base64.urlsafe_b64encode(public_key_pem).decode("utf-8")

    return {
        "service-info": {
            "name": "fakerealestate.com",
            "description": "A fictional service providing property listings "
            "and real estate data.",
            "service_url": f"{base_url}",
            "service_logo_url": f"{base_url}/logo.png",
            "service_terms_of_service_url": f"{base_url}/terms",
            "service_privacy_policy_url": f"{base_url}/privacy",
        },
        "intents": [
            {
                "intent_uid": "fakerealestate.com:searchProperty:v1",
                "intent_name": "SearchProperty",
                "description": (
                    "Searches properties based on location, price range, "
                    "and property type."
                ),
                "input_parameters": SearchRequest.model_json_schema()["properties"],
                "output_parameters": SearchResponse.model_json_schema()["properties"],
                "tags": ["real estate", "search", "property"],
                "rate_limit": "1000/hour",
                "price": "0.00 USD",
            },
            {
                "intent_uid": "fakerealestate.com:getPropertyDetails:v1",
                "intent_name": "GetPropertyDetails",
                "description": (
                    "Fetches detailed information for a specific property "
                    "based on property ID."
                ),
                "input_parameters": DetailsRequest.model_json_schema()["properties"],
                "output_parameters": DetailsResponse.model_json_schema()["properties"],
                "tags": ["real estate", "details", "property"],
                "rate_limit": "1000/hour",
                "price": "0.01 USD",
            },
        ],
        "uim-public-key": public_key_base64url,
        "uim-policy-file": f"{base_url}/uim-policy.json",
        "uim-api-discovery": f"{base_url}/uim/intents/search",
        "uim-api-execute": f"{base_url}/uim/execute",
        "uim-compliance": {
            "standards": ["ISO27001", "GDPR"],
            "regional-compliance": {"EU": "GDPR", "US-CA": "CCPA"},
            "notes": "Data is encrypted in transit and at rest.",
        },
        "uim-license": UIM_SERVICE_LICENSE,
    }


@app.get("/uim-policy.json")
async def get_policy_json(request: Request):
    """
    Endpoint to retrieve the UIM policy in ODRL format.

    Args:
        request: The FastAPI request object

    Returns:
        JSONResponse: The policy JSON content
    """
    policy_json = create_policy_json(request)
    return JSONResponse(content=policy_json)


def create_policy_json(request: Request):
    """
    Create the ODRL policy JSON content.

    Args:
        request: The FastAPI request object

    Returns:
        dict: The policy JSON content
    """
    base_url = f"{request.url.scheme}://{request.client.host}:{request.url.port}"

    return {
        "@context": "http://www.w3.org/ns/odrl.jsonld",
        "@type": "odrl:Set",
        "@id": f"{base_url}/uim-policy",
        "profile": "http://www.w3.org/ns/odrl/2/core",
        "permission": [
            {
                "target": f"{base_url}/uim/execute/SearchProperty",
                "action": {
                    "id": "odrl:execute",
                    "refinement": [
                        {
                            "leftOperand": "odrl:count",
                            "operator": "odrl:lteq",
                            "rightOperand": 1000,
                            "unit": "odrl:hour",
                        }
                    ],
                },
            },
            {
                "target": f"{base_url}/uim/execute/GetPropertyDetails",
                "action": {
                    "id": "odrl:execute",
                    "refinement": [
                        {
                            "leftOperand": "odrl:count",
                            "operator": "odrl:lteq",
                            "rightOperand": 1000,
                            "unit": "odrl:hour",
                        }
                    ],
                },
                "duty": [
                    {
                        "action": [
                            {
                                "rdf:value": {"@id": "odrl:compensate"},
                                "refinement": [
                                    {
                                        "leftOperand": "payAmount",
                                        "operator": "eq",
                                        "rightOperand": {
                                            "@value": "0.01",
                                            "@type": "xsd:decimal",
                                        },
                                        "unit": "http://dbpedia.org/resource/Euro",
                                    }
                                ],
                            }
                        ]
                    }
                ],
            },
        ],
        "prohibition": [
            {
                "target": [
                    f"{base_url}/uim/execute/SearchProperty",
                    f"{base_url}/uim/execute/GetPropertyDetails",
                ],
                "action": {
                    "id": "odrl:execute",
                    "refinement": [
                        {
                            "leftOperand": "odrl:count",
                            "operator": "odrl:gt",
                            "rightOperand": 1000,
                            "unit": "odrl:hour",
                        }
                    ],
                },
            }
        ],
        "party": [
            {"function": "odrl:assigner", "identifier": f"{base_url}/assigner"},
            {"function": "odrl:assignee", "identifier": f"{base_url}/assignee"},
        ],
        "asset": [
            {"id": f"{base_url}/uim/execute/SearchProperty", "type": "odrl:Asset"},
            {"id": f"{base_url}/uim/execute/GetPropertyDetails", "type": "odrl:Asset"},
        ],
    }


def verify_signed_policy(signed_policy: str, agent_public_key: str) -> Dict:
    """
    Verify a signed policy using the agent's public key.

    Args:
        signed_policy: The JWT-encoded signed policy
        agent_public_key: The agent's public key in Base64URL format

    Returns:
        bool: True if verification succeeds, False otherwise
    """
    try:
        # Decode the Base64URL-encoded public key string back to bytes
        decoded_public_key = base64.urlsafe_b64decode(agent_public_key)

        # Load the decoded bytes into a _RSAPublicKey object
        public_key = serialization.load_pem_public_key(
            decoded_public_key, backend=default_backend()
        )
        # Decode and verify the signed policy
        decoded_policy = jwt.decode(signed_policy, public_key, algorithms=["RS256"])
        print(f"Verification successful for policy: {decoded_policy}")
        return True
    except jwt.ExpiredSignatureError as e:
        print("Error during policy verification: " f"Signature has expired. Error: {e}")
        return False
    except jwt.InvalidTokenError as e:
        print(f"Error during policy verification: Invalid token. Error: {e}")
        return False


def verify_pat(request: Request):
    """
    Verify a Policy Adherence Token (PAT) from the request's Authorization header.

    Args:
        request: The FastAPI request object

    Returns:
        dict: The decoded PAT payload

    Raises:
        HTTPException: If the PAT is invalid, expired, or missing
    """
    authorization_header = request.headers.get("Authorization")
    if not authorization_header:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Split the Authorization header into token type and token
    parts = authorization_header.split(" ")
    if len(parts) != 2:
        raise HTTPException(
            status_code=401, detail="Invalid Authorization header format"
        )

    token = parts[1]

    try:
        # Decode the token without verification to extract the payload
        decoded_pat = jwt.decode(token, options={"verify_signature": False})
        private_key, _ = get_key_pair(True)

        # Verify the token's signature
        jwt.decode(
            token,
            private_key,
            algorithms=["HS256"],
            options={"verify_aud": False},
        )

        # Check if the PAT is expired
        if datetime.fromisoformat(decoded_pat["valid_to"]) < datetime.now(timezone.utc):
            raise HTTPException(status_code=403, detail="PAT expired.")

        # Additional checks can be added here, such as permissions and obligations
        print(f"Verification successful for PAT: {decoded_pat}")

    except jwt.InvalidTokenError as e:  # Invalid token
        raise HTTPException(status_code=403, detail=f"Invalid PAT: {e}") from e

    return decoded_pat


@app.post("/pat/issue")
async def issue_pat(request: PolicyAgreementRequest):
    """
    Endpoint to issue a Policy Adherence Token (PAT).

    This endpoint verifies the signed policy and issues a PAT if valid.

    Args:
        request: The PolicyAgreementRequest containing the agent ID, signed policy,
                and agent public key

    Returns:
        dict: A dictionary containing the issued PAT

    Raises:
        HTTPException: If the policy verification fails or required fields are missing
    """
    print(f"Received policy agreement request: {request}")

    if not request.signed_policy:
        raise HTTPException(status_code=400, detail="Missing policy agreement.")
    if not request.agent_public_key:
        raise HTTPException(status_code=400, detail="Missing agent public key.")
    if not request.agent_id:
        raise HTTPException(status_code=400, detail="Missing agent id.")

    # Verify the signed policy
    if not verify_signed_policy(request.signed_policy, request.agent_public_key):
        raise HTTPException(status_code=400, detail="Policy verification failed.")

    # Generate and sign a PAT
    pat = {
        "uid": f"uim-pat-{uuid.uuid4()}",
        "issued_to": request.agent_id,
        "policy_reference": "uim-policy.json",
        "valid_from": datetime.now(timezone.utc).isoformat(),
        "valid_to": (datetime.now(timezone.utc) + timedelta(days=365)).isoformat(),
    }
    private_key, _ = get_key_pair(True)
    token = jwt.encode(pat, private_key, algorithm="HS256")
    return {"uim-pat": token}


# Define the security scheme
security_scheme = HTTPBearer()


@app.post("/uim/execute", dependencies=[Depends(security_scheme)])
async def execute_intent(request: ExecuteRequest, _: dict = Depends(verify_pat)):
    """
    Endpoint to execute an intent.

    This endpoint executes the specified intent with the provided parameters.
    It requires a valid PAT in the Authorization header.

    Args:
        request: The ExecuteRequest containing the intent UID and parameters
        _: The decoded PAT payload (injected by the verify_pat dependency but not used)

    Returns:
        JSONResponse: The intent execution result

    Raises:
        HTTPException: If the intent UID is unknown
    """
    # The PAT is verified by the dependency but not used in this function
    intent_uid = request.intent_uid
    parameters = request.parameters

    if intent_uid == "fakerealestate.com:searchProperty:v1":
        location = parameters.get("location")
        property_type = parameters.get("property_type")
        # These parameters are not used in this simple implementation
        # but would be in a real one
        # min_price = parameters.get("min_price")
        # max_price = parameters.get("max_price")

        # Simulate a search operation
        if location == "New York" and property_type == "apartment":
            response = {
                "total_results": 1,
                "properties": [
                    {
                        "property_id": "123",
                        "name": "Luxury Apartment",
                        "price": 2000,
                        "location": "New York",
                        "property_type": "apartment",
                    }
                ],
            }
        else:
            response = {"total_results": 0, "properties": []}
    elif intent_uid == "fakerealestate.com:getPropertyDetails:v1":
        property_id = parameters.get("property_id")

        # Simulate fetching property details
        if property_id == "123":
            response = {
                "property_details": {
                    "property_id": "123",
                    "name": "Luxury Apartment",
                    "price": 2000,
                    "location": "New York",
                    "property_type": "apartment",
                    "description": "A luxurious apartment in the heart of New York.",
                }
            }
        else:
            response = {"property_details": {}}
    else:
        raise HTTPException(status_code=400, detail="Unknown intent_uid")

    return JSONResponse(content=response)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=4000)
