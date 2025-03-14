# AI Agent Implementation Guide

This guide provides step-by-step instructions for implementing the UIM Protocol in an AI agent. It covers discovery, policy adherence, and intent execution.

## Overview

AI agents use the UIM Protocol to discover and interact with web services through well-defined intents. This guide will walk you through the process of implementing the UIM Protocol in your AI agent, from discovery to execution.

## Prerequisites

Before implementing the UIM Protocol in your AI agent, you should have:

- A basic understanding of the UIM Protocol concepts (intents, metadata, PATs)
- A development environment for your AI agent
- Knowledge of HTTP requests and JSON processing
- Cryptographic capabilities for signing and verifying signatures

## Implementation Steps

### 1. Set Up Your Development Environment

First, set up your development environment with the necessary libraries for HTTP requests, JSON processing, and cryptography. Here's an example using Python:

```python
# Required libraries
import requests
import json
import jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.hashes import SHA256
```

### 2. Generate Key Pair

Generate an RSA key pair for your AI agent. This will be used for signing policies and verifying signatures:

```python
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
```

### 3. Implement Service Discovery

Implement service discovery using DNS TXT records and `agents.json` files:

```python
def discover_service(domain):
    """
    Discover a service using DNS TXT records and agents.json
    """
    try:
        # In a real implementation, this would use DNS queries
        # For simplicity, we'll simulate it
        agents_json_url = f"https://{domain}/agents.json"
        return fetch_agents_json(agents_json_url)
    except Exception as e:
        print(f"Error discovering service: {e}")
        return None

def fetch_agents_json(url):
    """
    Fetch and parse the agents.json file
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching agents.json: {e}")
        return None
```

### 4. Implement Intent Discovery

Implement intent discovery using the service's discovery endpoint:

```python
def search_intents(service_url, query=None, tags=None):
    """
    Search for intents using the service's discovery endpoint
    """
    # Build query parameters
    params = {}
    if query:
        params["query"] = query
    if tags:
        params["tags"] = ",".join(tags)
    
    try:
        response = requests.get(
            f"{service_url}/uim/intents/search",
            params=params
        )
        response.raise_for_status()
        return response.json()["intents"]
    except Exception as e:
        print(f"Error searching intents: {e}")
        return []
```

### 5. Implement Policy Retrieval and PAT Acquisition

Implement policy retrieval and PAT acquisition:

```python
def get_policy(policy_url):
    """
    Retrieve the policy from the service
    """
    try:
        response = requests.get(policy_url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching policy: {e}")
        return None

def sign_policy(policy, private_key):
    """
    Sign the policy using the private key
    """
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
    """
    Request a PAT from the service
    """
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
```

### 6. Implement Intent Execution

Implement intent execution:

```python
def execute_intent(service_url, intent_uid, parameters, pat):
    """
    Execute an intent
    """
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
```

### 7. Put It All Together

Now, let's put it all together in a complete AI agent implementation:

```python
class UIMAgent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.private_key, self.public_key = generate_key_pair()
        self.pats = {}  # Store PATs for different services
        
    def discover_service(self, domain):
        return discover_service(domain)
    
    def search_intents(self, service_url, query=None, tags=None):
        return search_intents(service_url, query, tags)
    
    def get_policy(self, policy_url):
        return get_policy(policy_url)
    
    def sign_policy(self, policy):
        return sign_policy(policy, self.private_key)
    
    def request_pat(self, service_url, signed_policy):
        pat = request_pat(service_url, self.agent_id, signed_policy, self.public_key)
        if pat:
            self.pats[service_url] = pat
        return pat
    
    def execute_intent(self, service_url, intent_uid, parameters):
        pat = self.pats.get(service_url)
        if not pat:
            print(f"No PAT available for {service_url}")
            return None
        
        return execute_intent(service_url, intent_uid, parameters, pat)
    
    def interact_with_service(self, domain, query=None, tags=None):
        """
        High-level method to interact with a service
        """
        # Discover service
        service_info = self.discover_service(domain)
        if not service_info:
            return None
        
        # Get service details
        policy_url = service_info["uim-policy-file"]
        service_url = service_info["service-info"]["service_url"]
        
        # Get policy and request PAT
        policy = self.get_policy(policy_url)
        if not policy:
            return None
        
        signed_policy = self.sign_policy(policy)
        pat = self.request_pat(service_url, signed_policy)
        if not pat:
            return None
        
        # Search for intents
        intents = self.search_intents(service_url, query, tags)
        return intents
    
    def execute_intent_by_name(self, domain, intent_name, parameters):
        """
        Execute an intent by name
        """
        # Discover service
        service_info = self.discover_service(domain)
        if not service_info:
            return None
        
        # Get service details
        policy_url = service_info["uim-policy-file"]
        service_url = service_info["service-info"]["service_url"]
        
        # Get policy and request PAT if needed
        if service_url not in self.pats:
            policy = self.get_policy(policy_url)
            if not policy:
                return None
            
            signed_policy = self.sign_policy(policy)
            pat = self.request_pat(service_url, signed_policy)
            if not pat:
                return None
        
        # Search for the intent
        intents = self.search_intents(service_url, intent_name=intent_name)
        if not intents:
            return None
        
        # Find the intent with the matching name
        intent = next((i for i in intents if i["intent_name"] == intent_name), None)
        if not intent:
            return None
        
        # Execute the intent
        return self.execute_intent(service_url, intent["intent_uid"], parameters)
```

## Example Usage

Here's an example of how to use the UIM agent to interact with a web service:

```python
# Create an AI agent
agent = UIMAgent("ai-agent-123")

# Interact with a service
intents = agent.interact_with_service("example.com", tags=["e-commerce", "search"])

# Print available intents
for intent in intents:
    print(f"Intent: {intent['intent_name']}")
    print(f"Description: {intent['description']}")
    print(f"UID: {intent['intent_uid']}")
    print("---")

# Execute an intent
result = agent.execute_intent_by_name(
    "example.com",
    "SearchProducts",
    {"query": "laptop", "category": "electronics"}
)

# Process the result
if result:
    print(f"Found {result['total_results']} products:")
    for product in result['products']:
        print(f"- {product['name']} (${product['price']})")
```

## Error Handling

When implementing the UIM Protocol, it's important to handle errors properly. Here are some common errors and how to handle them:

### Discovery Errors

- **DNS Resolution Errors**: Handle DNS resolution errors by providing clear error messages and fallback mechanisms.
- **Network Errors**: Handle network errors by implementing retry logic with exponential backoff.

### Policy and PAT Errors

- **Policy Retrieval Errors**: Handle policy retrieval errors by providing clear error messages and fallback mechanisms.
- **PAT Issuance Errors**: Handle PAT issuance errors by checking the error response and taking appropriate action.

### Intent Execution Errors

- **Validation Errors**: Handle validation errors by checking the input parameters before sending the request.
- **Execution Errors**: Handle execution errors by checking the error response and taking appropriate action.
- **Rate Limiting Errors**: Handle rate limiting errors by implementing retry logic with exponential backoff.

## Best Practices

Here are some best practices for implementing the UIM Protocol in your AI agent:

### Security

- **Secure Key Storage**: Store private keys securely, using hardware security modules (HSMs) when possible.
- **Policy Validation**: Validate policies before agreeing to them, ensuring they are reasonable and do not pose security risks.
- **PAT Management**: Securely store PATs and renew them before they expire.

### Performance

- **Caching**: Cache discovery results, policies, and PATs to reduce the number of network requests.
- **Connection Pooling**: Use connection pooling to reduce the overhead of establishing new connections.
- **Asynchronous Requests**: Use asynchronous requests to improve performance when making multiple requests.

### Reliability

- **Retry Logic**: Implement retry logic with exponential backoff for transient errors.
- **Circuit Breakers**: Implement circuit breakers to prevent cascading failures.
- **Fallbacks**: Implement fallback mechanisms for critical functionality.

## Conclusion

By following this guide, you should now have a basic understanding of how to implement the UIM Protocol in your AI agent. Remember to handle errors properly, follow best practices, and test your implementation thoroughly.

For more information, refer to the [UIM Protocol Specification](../specification/index.md) and the [API Reference](../reference/api-reference.md).
