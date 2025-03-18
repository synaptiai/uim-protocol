# Appendix

This appendix provides additional information, references, and resources related to the UIM Protocol.

## 1. Glossary

### 1.1 Key Terms

| Term | Definition |
|------|------------|
| **AI Agent** | A software application or service that uses artificial intelligence to perform tasks on behalf of users. In the context of the UIM Protocol, AI agents discover and execute intents provided by web services. |
| **Intent** | A predefined action that an AI agent can perform on a web service. Intents encapsulate specific tasks, including necessary parameters and execution details. |
| **Metadata** | Descriptive information about an intent, including its name, description, and category. |
| **Parameter** | Input or output data required for an intent's execution. Parameters have names, types, and may be required or optional. |
| **Policy Adherence Token (PAT)** | A digitally signed token issued by a web service to an AI agent, encapsulating permissions, usage limits, and billing agreements. |
| **Service** | A web service that publishes its capabilities (intents) using the UIM Protocol. |
| **Endpoint** | The API endpoint where an intent can be executed. |
| **Discovery** | The process by which AI agents find available intents and services. |
| **Execution** | The process of performing an intent, including parameter validation, action execution, and response formatting. |
| **ODRL** | Open Digital Rights Language, a policy expression language used to define permissions, prohibitions, and obligations in the UIM Protocol. |

### 1.2 Acronyms

| Acronym | Full Form |
|---------|-----------|
| **UIM** | Unified Intent Mediator |
| **PAT** | Policy Adherence Token |
| **JWT** | JSON Web Token |
| **ODRL** | Open Digital Rights Language |
| **TLS** | Transport Layer Security |
| **API** | Application Programming Interface |
| **JSON** | JavaScript Object Notation |
| **DNS** | Domain Name System |
| **HTTP** | Hypertext Transfer Protocol |
| **HTTPS** | HTTP Secure |

## 2. References

### 2.1 Standards and Specifications

- [JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519)
- [Open Digital Rights Language (ODRL) Information Model 2.2](https://www.w3.org/TR/odrl-model/)
- [HTTP/1.1](https://datatracker.ietf.org/doc/html/rfc7231)
- [HTTP/2](https://datatracker.ietf.org/doc/html/rfc7540)
- [Transport Layer Security (TLS)](https://datatracker.ietf.org/doc/html/rfc8446)
- [DNS TXT Records](https://datatracker.ietf.org/doc/html/rfc1464)
- [JSON Schema](https://json-schema.org/)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)

### 2.2 Related Technologies

- [OAuth 2.0](https://oauth.net/2/)
- [OpenID Connect](https://openid.net/connect/)
- [JSON-LD](https://json-ld.org/)
- [WebSub](https://www.w3.org/TR/websub/)
- [Activity Streams](https://www.w3.org/TR/activitystreams-core/)
- [Schema.org](https://schema.org/)

## 3. Example Implementations

### 3.1 AI Agent Implementation

```python
import requests
import jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.hashes import SHA256

class UIMAgent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.private_key, self.public_key = self._generate_key_pair()
        self.pats = {}  # Store PATs for different services

    def _generate_key_pair(self):
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

    def discover_service(self, domain):
        # Query DNS TXT records
        try:
            # In a real implementation, this would use DNS queries
            # For simplicity, we'll simulate it
            agents_json_url = f"https://{domain}/agents.json"
            return self.fetch_agents_json(agents_json_url)
        except Exception as e:
            print(f"Error discovering service: {e}")
            return None

    def fetch_agents_json(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching agents.json: {e}")
            return None

    def get_policy(self, policy_url):
        try:
            response = requests.get(policy_url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching policy: {e}")
            return None

    def sign_policy(self, policy):
        # Sign the policy using the private key
        private_key_obj = serialization.load_pem_private_key(
            self.private_key,
            password=None
        )
        policy_json = json.dumps(policy).encode('utf-8')
        signature = private_key_obj.sign(
            policy_json,
            padding.PKCS1v15(),
            SHA256()
        )
        return signature

    def request_pat(self, service_url, signed_policy):
        try:
            response = requests.post(
                f"{service_url}/pat/issue",
                json={
                    "agent_id": self.agent_id,
                    "signed_policy": signed_policy.hex(),
                    "agent_public_key": self.public_key.decode('utf-8')
                }
            )
            response.raise_for_status()
            pat = response.json()["uim-pat"]
            self.pats[service_url] = pat
            return pat
        except Exception as e:
            print(f"Error requesting PAT: {e}")
            return None

    def execute_intent(self, service_url, intent_uid, parameters):
        # Get PAT for the service
        pat = self.pats.get(service_url)
        if not pat:
            print(f"No PAT available for {service_url}")
            return None

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

    def search_intents(self, service_url, query=None, tags=None):
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

# Example usage
agent = UIMAgent("ai-agent-123")
service_info = agent.discover_service("example.com")

if service_info:
    policy_url = service_info["uim-policy-file"]
    service_url = service_info["service-info"]["service_url"]

    policy = agent.get_policy(policy_url)
    if policy:
        signed_policy = agent.sign_policy(policy)
        pat = agent.request_pat(service_url, signed_policy)

        if pat:
            # Search for intents
            intents = agent.search_intents(service_url, tags=["e-commerce", "search"])

            if intents:
                # Execute an intent
                intent_uid = intents[0]["intent_uid"]
                result = agent.execute_intent(
                    service_url,
                    intent_uid,
                    {"query": "laptop"}
                )

                if result:
                    print(f"Intent execution result: {result}")
```

### 3.2 Web Service Implementation

```python
from flask import Flask, request, jsonify
import jwt
import json
import time
import uuid
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.hashes import SHA256

app = Flask(__name__)

# Generate RSA key pair for the service
private_key, public_key = generate_key_pair()

# Define intents
intents = [
    {
        "intent_uid": "example.com:search-products:v1",
        "intent_name": "SearchProducts",
        "description": "Search for products based on criteria",
        "input_parameters": [
            {"name": "query", "type": "string", "required": True},
            {"name": "category", "type": "string", "required": False},
            {"name": "price_range", "type": "string", "required": False},
            {"name": "sort_by", "type": "string", "required": False}
        ],
        "output_parameters": [
            {"name": "products", "type": "array", "required": True},
            {"name": "total_results", "type": "integer", "required": True}
        ],
        "endpoint": "https://api.example.com/products/search",
        "tags": ["e-commerce", "search", "products"]
    }
]

# Define policy
policy = {
    "@context": "http://www.w3.org/ns/odrl.jsonld",
    "uid": "http://example.com/policy/12345",
    "type": "Set",
    "profile": "http://example.com/profile/odrl-uim",
    "permission": [
        {
            "target": "http://example.com/api/intents",
            "action": "execute",
            "constraint": [
                {
                    "leftOperand": "http://example.com/vocab/rateLimit",
                    "operator": "lte",
                    "rightOperand": 1000,
                    "unit": "http://example.com/vocab/hour"
                }
            ],
            "duty": [
                {
                    "action": "pay",
                    "target": "http://example.com/vocab/intentPrice",
                    "amount": 0.01,
                    "unit": "http://example.com/vocab/USD"
                }
            ]
        }
    ]
}

@app.route("/agents.json")
def agents_json():
    return jsonify({
        "service-info": {
            "name": "Example E-commerce Service",
            "description": "Provides e-commerce functionalities",
            "service_url": "https://api.example.com",
            "service_logo_url": "https://example.com/logo.png",
            "service_terms_of_service_url": "https://example.com/terms",
            "service_privacy_policy_url": "https://example.com/privacy"
        },
        "intents": intents,
        "uim-public-key": public_key.decode('utf-8'),
        "uim-policy-file": "https://example.com/uim-policy.json",
        "uim-api-discovery": "https://api.example.com/uim/intents/search",
        "uim-compliance": {
            "standards": ["ISO27001", "GDPR"],
            "regional-compliance": {
                "EU": "GDPR",
                "US-CA": "CCPA"
            },
            "notes": "Data is encrypted in transit and at rest."
        }
    })

@app.route("/uim-policy.json")
def uim_policy():
    return jsonify(policy)

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

    return jsonify({
        "uim-pat": token,
        "expires_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(pat["exp"]))
    })

@app.route("/uim/intents/search")
def search_intents():
    query = request.args.get("query")
    tags = request.args.get("tags")

    filtered_intents = intents

    if query:
        filtered_intents = [
            intent for intent in filtered_intents
            if query.lower() in intent["intent_name"].lower() or
               query.lower() in intent["description"].lower()
        ]

    if tags:
        tag_list = tags.split(",")
        filtered_intents = [
            intent for intent in filtered_intents
            if any(tag in intent["tags"] for tag in tag_list)
        ]

    return jsonify({
        "intents": filtered_intents,
        "pagination": {
            "total_results": len(filtered_intents),
            "total_pages": 1,
            "current_page": 1,
            "page_size": len(filtered_intents)
        }
    })

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

def verify_signed_policy(signed_policy_hex, agent_public_key_pem):
    try:
        # Convert hex to bytes
        signed_policy = bytes.fromhex(signed_policy_hex)

        # Load agent's public key
        agent_public_key = serialization.load_pem_public_key(
            agent_public_key_pem.encode('utf-8')
        )

        # Load policy
        policy_json = json.dumps(policy).encode('utf-8')

        # Verify signature
        agent_public_key.verify(
            signed_policy,
            policy_json,
            padding.PKCS1v15(),
            SHA256()
        )

        return True
    except Exception as e:
        print(f"Error verifying signed policy: {e}")
        return False

def verify_pat(pat):
    try:
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
```

## 4. JSON Schemas

### 4.1 Intent Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Intent",
  "description": "A UIM Protocol intent",
  "type": "object",
  "required": [
    "intent_uid",
    "intent_name",
    "description",
    "input_parameters",
    "output_parameters",
    "endpoint"
  ],
  "properties": {
    "intent_uid": {
      "type": "string",
      "description": "The unique identifier for the intent",
      "pattern": "^[a-zA-Z0-9.-]+:[a-z0-9-]+:v[0-9]+(\\.[0-9]+)*$"
    },
    "intent_name": {
      "type": "string",
      "description": "The name of the intent"
    },
    "description": {
      "type": "string",
      "description": "A description of the intent"
    },
    "input_parameters": {
      "type": "array",
      "description": "The input parameters for the intent",
      "items": {
        "$ref": "#/definitions/parameter"
      }
    },
    "output_parameters": {
      "type": "array",
      "description": "The output parameters for the intent",
      "items": {
        "$ref": "#/definitions/parameter"
      }
    },
    "endpoint": {
      "type": "object",
      "description": "The endpoint for the intent",
      "required": [
        "url",
        "method",
        "content_type"
      ],
      "properties": {
        "url": {
          "type": "string",
          "description": "The URL for the intent",
          "format": "uri"
        },
        "method": {
          "type": "string",
          "description": "The HTTP method for the intent",
          "enum": [
            "GET",
            "POST",
            "PUT",
            "DELETE",
            "PATCH"
          ]
        },
        "content_type": {
          "type": "string",
          "description": "The content type for the intent",
          "default": "application/json"
        }
      }
    },
    "tags": {
      "type": "array",
      "description": "Tags for the intent",
      "items": {
        "type": "string"
      }
    },
    "category": {
      "type": "string",
      "description": "The category for the intent"
    },
    "version": {
      "type": "string",
      "description": "The version of the intent",
      "pattern": "^v[0-9]+(\\.[0-9]+)*$"
    }
  },
  "definitions": {
    "parameter": {
      "type": "object",
      "required": [
        "name",
        "type"
      ],
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the parameter"
        },
        "type": {
          "type": "string",
          "description": "The type of the parameter",
          "enum": [
            "string",
            "number",
            "integer",
            "boolean",
            "array",
            "object",
            "null",
            "any"
          ]
        },
        "required": {
          "type": "boolean",
          "description": "Whether the parameter is required",
          "default": false
        },
        "description": {
          "type": "string",
          "description": "A description of the parameter"
        },
        "default": {
          "description": "The default value for the parameter"
        },
        "enum": {
          "type": "array",
          "description": "The allowed values for the parameter"
        },
        "minimum": {
          "type": "number",
          "description": "The minimum value for the parameter"
        },
        "maximum": {
          "type": "number",
          "description": "The maximum value for the parameter"
        },
        "minLength": {
          "type": "integer",
          "description": "The minimum length for the parameter",
          "minimum": 0
        },
        "maxLength": {
          "type": "integer",
          "description": "The maximum length for the parameter",
          "minimum": 0
        },
        "pattern": {
          "type": "string",
          "description": "The pattern for the parameter",
          "format": "regex"
        },
        "format": {
          "type": "string",
          "description": "The format for the parameter",
          "enum": [
            "date",
            "date-time",
            "email",
            "hostname",
            "ipv4",
            "ipv6",
            "uri",
            "uri-reference",
            "uuid"
          ]
        }
      }
    }
  }
}
```

### 4.2 `agents.json` Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "agents.json",
  "description": "A UIM Protocol agents.json file",
  "type": "object",
  "required": [
    "service-info",
    "intents",
    "uim-public-key",
    "uim-policy-file"
  ],
  "properties": {
    "service-info": {
      "type": "object",
      "description": "Information about the service",
      "required": [
        "name",
        "description",
        "service_url"
      ],
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the service"
        },
        "description": {
          "type": "string",
          "description": "A description of the service"
        },
        "service_url": {
          "type": "string",
          "description": "The URL of the service",
          "format": "uri"
        },
        "service_logo_url": {
          "type": "string",
          "description": "The URL of the service's logo",
          "format": "uri"
        },
        "service_terms_of_service_url": {
          "type": "string",
          "description": "The URL of the service's terms of service",
          "format": "uri"
        },
        "service_privacy_policy_url": {
          "type": "string",
          "description": "The URL of the service's privacy policy",
          "format": "uri"
        }
      }
    },
    "intents": {
      "type": "array",
      "description": "The intents provided by the service",
      "items": {
        "$ref": "#/definitions/intent"
      }
    },
    "uim-public-key": {
      "type": "string",
      "description": "The public key of the service"
    },
    "uim-policy-file": {
      "type": "string",
      "description": "The URL of the service's policy file",
      "format": "uri"
    },
    "uim-api-discovery": {
      "type": "string",
      "description": "The URL of the service's API discovery endpoint",
      "format": "uri"
    },
    "uim-compliance": {
      "type": "object",
      "description": "Compliance information for the service",
      "properties": {
        "standards": {
          "type": "array",
          "description": "The compliance standards the service adheres to",
          "items": {
            "type": "string"
          }
        },
        "regional-compliance": {
          "type": "object",
          "description": "Region-specific compliance information",
          "additionalProperties": {
            "type": "string"
          }
        },
        "notes": {
          "type": "string",
          "description": "Additional compliance notes"
        }
      }
    }
  },
  "definitions": {
    "intent": {
      "type": "object",
      "required": [
        "intent_uid",
        "intent_name",
        "description",
        "input_parameters",
        "output_parameters",
        "endpoint"
      ],
      "properties": {
        "intent_uid": {
          "type": "string",
          "description": "The unique identifier for the intent",
          "pattern": "^[a-zA-Z0-9.-]+:[a-z0-9-]+:v[0-9]+(\\.[0-9]+)*$"
        },
        "intent_name": {
          "type": "string",
          "description": "The name of the intent"
        },
        "description": {
          "type": "string",
          "description": "A description of the intent"
        },
        "input_parameters": {
          "type": "array",
          "description": "The input parameters for the intent",
          "items": {
            "$ref": "#/definitions/parameter"
          }
        },
        "output_parameters": {
          "type": "array",
          "description": "The output parameters for the intent",
          "items": {
            "$ref": "#/definitions/parameter"
          }
        },
        "endpoint": {
          "type": "object",
          "description": "The endpoint for the intent",
          "required": [
            "url",
            "method",
            "content_type"
          ],
          "properties": {
            "url": {
              "type": "string",
              "description": "The URL for the intent",
              "format": "uri"
            },
            "method": {
              "type": "string",
              "description": "The HTTP method for the intent",
              "enum": [
                "GET",
                "POST",
                "PUT",
                "DELETE",
                "PATCH"
              ]
            },
            "content_type": {
              "type": "string",
              "description": "The content type for the intent",
              "default": "application/json"
            }
          }
        },
        "tags": {
          "type": "array",
          "description": "Tags for the intent",
          "items": {
            "type": "string"
          }
        }
      }
    },
    "parameter": {
      "type": "object",
      "required": [
        "name",
        "type"
      ],
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the parameter"
        },
        "type": {
          "type": "string",
          "description": "The type of the parameter",
          "enum": [
            "string",
            "number",
            "integer",
            "boolean",
            "array",
            "object",
            "null",
            "any"
          ]
        },
        "required": {
          "type": "boolean",
          "description": "Whether the parameter is required",
          "default": false
        },
        "description": {
          "type": "string",
          "description": "A description of the parameter"
        }
      }
    }
  }
}
```

## 5. Future Directions

The UIM Protocol is an evolving standard, and several areas are being explored for future development:

### 5.1 Enhanced Discovery Mechanisms

- **Federated Discovery**: Enabling discovery across multiple repositories or networks.
- **Semantic Discovery**: Using semantic technologies to improve intent discovery and matching.
- **Context-Aware Discovery**: Taking into account the user's context when discovering intents.

### 5.2 Advanced Policy Management

- **Dynamic Policies**: Policies that can adapt based on context, usage patterns, or other factors.
- **Policy Negotiation**: Enabling AI agents and web services to negotiate policy terms.
- **Policy Federation**: Allowing policies to be shared and reused across services.

### 5.3 Interoperability

- **Cross-Protocol Bridges**: Enabling interoperability with other protocols and standards.
- **Legacy System Integration**: Providing mechanisms to integrate with legacy systems.
- **Multi-Modal Interactions**: Supporting interactions beyond HTTP, such as WebSockets, gRPC, or GraphQL.

### 5.4 Security and Privacy Enhancements

- **Zero-Knowledge Proofs**: Enabling verification without revealing sensitive information.
- **Differential Privacy**: Protecting user privacy while still allowing useful data analysis.
- **Decentralized Identity**: Integrating with decentralized identity systems.

### 5.5 Standardization

- **Formal Standardization**: Working towards formal standardization through organizations like W3C or IETF.
- **Reference Implementations**: Developing reference implementations in multiple programming languages.
- **Compliance Testing**: Creating tools and frameworks for testing compliance with the UIM Protocol.

## 6. Acknowledgments

The UIM Protocol is the result of collaborative efforts from many individuals and organizations. We would like to acknowledge the contributions of:

- The UIM Protocol Working Group
- The Open
