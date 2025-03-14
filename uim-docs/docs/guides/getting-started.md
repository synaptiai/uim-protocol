# Getting Started with the UIM Protocol

This guide will help you get started with implementing the UIM Protocol in your applications. Whether you're developing an AI agent or a web service, this guide will provide you with the information you need to begin.

## Prerequisites

Before you start implementing the UIM Protocol, you should have:

- Basic knowledge of web development and APIs
- Familiarity with JSON and HTTP
- Understanding of authentication and security concepts
- Development environment set up for your preferred programming language

## Implementation Overview

Implementing the UIM Protocol involves several steps, depending on whether you're developing an AI agent or a web service. Here's a high-level overview of the process:

### For AI Agents

1. **Discover Intents**: Implement mechanisms to discover available intents from web services.
2. **Agree to Policies**: Implement policy agreement and PAT management.
3. **Execute Intents**: Implement intent execution with proper authentication and error handling.

### For Web Services

1. **Define Intents**: Define the intents your service will offer, including metadata and parameters.
2. **Implement Discovery**: Set up discovery mechanisms like DNS TXT records and `agents.json` files.
3. **Manage Policies**: Implement policy management and PAT issuance.
4. **Execute Intents**: Implement intent execution endpoints with proper validation and error handling.

## Quick Start: AI Agent

Here's a quick guide to implementing a basic AI agent that can discover and execute intents:

### 1. Discover Intents

First, you need to discover available intents from web services. You can do this by querying DNS TXT records and retrieving `agents.json` files:

```python
import dns.resolver
import requests
import json

def discover_service(domain):
    # Query DNS TXT records
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            for txt_string in rdata.strings:
                txt_string = txt_string.decode('utf-8')
                if txt_string.startswith('uim-agents='):
                    agents_json_url = txt_string.split('=', 1)[1]
                    return fetch_agents_json(agents_json_url)
    except Exception as e:
        print(f"Error querying DNS: {e}")
    
    # Try default location
    return fetch_agents_json(f"https://{domain}/agents.json")

def fetch_agents_json(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching agents.json: {e}")
        return None

# Example usage
service_info = discover_service('example.com')
if service_info:
    print(f"Service: {service_info['service-info']['name']}")
    print(f"Intents: {len(service_info['intents'])}")
    for intent in service_info['intents']:
        print(f"  - {intent['intent_name']}: {intent['description']}")
```

### 2. Agree to Policies and Obtain PAT

Next, you need to agree to the service's policies and obtain a Policy Adherence Token (PAT):

```python
import jwt
import requests
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.hashes import SHA256

def generate_key_pair():
    # Generate RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    
    # Serialize keys
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    return private_pem, public_pem

def get_policy(policy_url):
    try:
        response = requests.get(policy_url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching policy: {e}")
        return None

def sign_policy(policy, private_key):
    # Sign the policy using the private key
    private_key_obj = serialization.load_pem_private_key(
        private_key,
        password=None
    )
    policy_json = json.dumps(policy).encode('utf-8')
    signature = private_key_obj.sign(
        policy_json,
        padding.PKCS1v15(),
        SHA256()
    )
    return signature

def request_pat(service_url, agent_id, signed_policy, public_key):
    try:
        response = requests.post(
            f"{service_url}/pat/issue",
            json={
                "agent_id": agent_id,
                "signed_policy": signed_policy.hex(),
                "agent_public_key": public_key.decode('utf-8')
            }
        )
        response.raise_for_status()
        return response.json()["uim-pat"]
    except Exception as e:
        print(f"Error requesting PAT: {e}")
        return None

# Example usage
private_key, public_key = generate_key_pair()
policy = get_policy("https://example.com/uim-policy.json")
if policy:
    signed_policy = sign_policy(policy, private_key)
    pat = request_pat(
        "https://api.example.com",
        "ai-agent-123",
        signed_policy,
        public_key
    )
    if pat:
        print(f"PAT obtained: {pat}")
```

### 3. Execute Intents

Finally, you can execute intents using the PAT:

```python
def execute_intent(service_url, intent_uid, parameters, pat):
    try:
        response = requests.post(
            f"{service_url}/uim/execute",
            headers={
                "Authorization": f"Bearer {pat}",
                "Content-Type": "application/json"
            },
            json={
                "intent_uid": intent_uid,
                "parameters": parameters
            }
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error executing intent: {e}")
        return None

# Example usage
result = execute_intent(
    "https://api.example.com",
    "example.com:search-products:v1",
    {"query": "laptop"},
    pat
)
if result:
    print(f"Result: {result}")
```

## Quick Start: Web Service

Here's a quick guide to implementing a basic web service that offers intents:

### 1. Define Intents

First, define the intents your service will offer:

```python
intents = [
    {
        "intent_uid": "example.com:search-products:v1",
        "intent_name": "SearchProducts",
        "description": "Search for products based on criteria",
        "input_parameters": [
            {
                "name": "query",
                "type": "string",
                "required": True,
                "description": "Search query string"
            }
        ],
        "output_parameters": [
            {
                "name": "products",
                "type": "array",
                "description": "List of matching products"
            }
        ],
        "endpoint": {
            "url": "https://api.example.com/products/search",
            "method": "POST",
            "content_type": "application/json"
        },
        "tags": [
            "e-commerce",
            "search",
            "products"
        ]
    }
]
```

### 2. Set Up Discovery

Next, set up discovery mechanisms:

#### DNS TXT Records

Add the following TXT records to your domain:

```
_uim.example.com. IN TXT "uim-agents=https://example.com/agents.json"
_uim.example.com. IN TXT "uim-discovery=https://api.example.com/discovery"
_uim.example.com. IN TXT "uim-policy=https://example.com/policy.json"
```

#### `agents.json` File

Create an `agents.json` file with information about your service and intents:

```python
import json
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def generate_key_pair():
    # Generate RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    
    # Serialize keys
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    return private_pem, public_pem

def create_agents_json(service_name, service_description, service_url, intents):
    private_key, public_key = generate_key_pair()
    
    # Save private key to file
    with open("private_key.pem", "wb") as f:
        f.write(private_key)
    
    agents_json = {
        "service-info": {
            "name": service_name,
            "description": service_description,
            "service_url": service_url,
            "service_logo_url": f"{service_url}/logo.png",
            "service_terms_of_service_url": f"{service_url}/terms",
            "service_privacy_policy_url": f"{service_url}/privacy"
        },
        "intents": intents,
        "uim-public-key": public_key.decode('utf-8'),
        "uim-policy-file": f"{service_url}/uim-policy.json",
        "uim-api-discovery": f"{service_url}/uim/intents/search",
        "uim-compliance": {
            "standards": ["ISO27001", "GDPR"],
            "regional-compliance": {
                "EU": "GDPR",
                "US-CA": "CCPA"
            },
            "notes": "Data is encrypted in transit and at rest."
        }
    }
    
    # Save agents.json to file
    with open("agents.json", "w") as f:
        json.dump(agents_json, f, indent=2)
    
    return agents_json

# Example usage
agents_json = create_agents_json(
    "Example E-commerce Service",
    "Provides e-commerce functionalities",
    "https://api.example.com",
    intents
)
```

### 3. Implement Policy Management and PAT Issuance

Implement policy management and PAT issuance:

```python
import jwt
import json
import time
import uuid
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.hashes import SHA256
from flask import Flask, request, jsonify

app = Flask(__name__)

def load_private_key():
    with open("private_key.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=None
        )
    return private_key

def verify_signed_policy(signed_policy_hex, agent_public_key_pem):
    try:
        # Convert hex to bytes
        signed_policy = bytes.fromhex(signed_policy_hex)
        
        # Load agent's public key
        agent_public_key = serialization.load_pem_public_key(
            agent_public_key_pem.encode('utf-8')
        )
        
        # Load policy
        with open("uim-policy.json", "rb") as f:
            policy = f.read()
        
        # Verify signature
        agent_public_key.verify(
            signed_policy,
            policy,
            padding.PKCS1v15(),
            SHA256()
        )
        
        return True
    except Exception as e:
        print(f"Error verifying signed policy: {e}")
        return False

@app.route("/pat/issue", methods=["POST"])
def issue_pat():
    data = request.json
    agent_id = data.get("agent_id")
    signed_policy = data.get("signed_policy")
    agent_public_key = data.get("agent_public_key")
    
    if not agent_id or not signed_policy or not agent_public_key:
        return jsonify({"error": "Missing required parameters"}), 400
    
    if not verify_signed_policy(signed_policy, agent_public_key):
        return jsonify({"error": "Invalid policy signature"}), 400
    
    # Generate PAT
    private_key = load_private_key()
    pat = {
        "iss": "example.com",
        "sub": agent_id,
        "exp": int(time.time()) + 86400,  # 24 hours
        "nbf": int(time.time()),
        "jti": str(uuid.uuid4()),
        "scope": ["example.com:search-products:v1:execute"],
        "pol": "https://example.com/uim-policy.json",
        "lmt": {
            "rate": 100,
            "period": 3600
        }
    }
    
    # Sign PAT
    token = jwt.encode(pat, private_key, algorithm="RS256")
    
    return jsonify({"uim-pat": token})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
```

### 4. Implement Intent Execution

Finally, implement intent execution:

```python
import jwt
from flask import Flask, request, jsonify

app = Flask(__name__)

def verify_pat(pat):
    try:
        # Load public key
        with open("public_key.pem", "rb") as f:
            public_key = f.read()
        
        # Verify PAT
        decoded_pat = jwt.decode(
            pat,
            public_key,
            algorithms=["RS256"],
            options={"verify_aud": False}
        )
        
        return decoded_pat
    except Exception as e:
        print(f"Error verifying PAT: {e}")
        return None

@app.route("/uim/execute", methods=["POST"])
def execute_intent():
    # Get PAT from Authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Missing or invalid Authorization header"}), 401
    
    pat = auth_header.split(" ")[1]
    decoded_pat = verify_pat(pat)
    if not decoded_pat:
        return jsonify({"error": "Invalid PAT"}), 401
    
    # Get intent and parameters
    data = request.json
    intent_uid = data.get("intent_uid")
    parameters = data.get("parameters", {})
    
    if not intent_uid:
        return jsonify({"error": "Missing intent_uid"}), 400
    
    # Check if intent is allowed by PAT
    if f"{intent_uid}:execute" not in decoded_pat.get("scope", []):
        return jsonify({"error": "Intent not allowed by PAT"}), 403
    
    # Execute intent
    if intent_uid == "example.com:search-products:v1":
        query = parameters.get("query")
        if not query:
            return jsonify({"error": "Missing required parameter: query"}), 400
        
        # Simulate search
        products = [
            {
                "id": "123",
                "name": "Laptop",
                "price": 1000,
                "description": "A powerful laptop"
            }
        ]
        
        return jsonify({
            "products": products,
            "total_results": len(products)
        })
    else:
        return jsonify({"error": "Unknown intent"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
```

## Next Steps

Now that you have a basic understanding of how to implement the UIM Protocol, you can:

- Explore the [AI Agent Guide](ai-agent-guide.md) for more detailed information on implementing an AI agent.
- Check out the [Service Provider Guide](service-provider-guide.md) for more detailed information on implementing a web service.
- See the [Integration Examples](integration-examples.md) for real-world examples of UIM Protocol integration.
- Refer to the [Specification](../specification/overview.md) for detailed information about the protocol.

## Resources

- [UIM Protocol GitHub Repository](https://github.com/synaptiai/uim-protocol)
- [UIM Protocol Discord Server](https://discord.gg/uimprotocol)
- [UIM Protocol Twitter](https://twitter.com/uimprotocol)
