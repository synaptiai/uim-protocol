# UIM Protocol API Documentation

This directory contains documentation for the UIM Protocol APIs. These APIs define how AI agents and web services interact using the protocol.

## API Overview

The UIM Protocol defines three main types of APIs:

1. **Discovery API**: Used by AI agents to discover available intents from web services.
2. **Execution API**: Used by AI agents to execute intents on web services.
3. **Policy API**: Used by AI agents to retrieve policies and request Policy Adherence Tokens (PATs) from web services.

## Discovery API

The Discovery API allows AI agents to search for and retrieve information about available intents.

### Endpoints

#### Search Intents

- **Endpoint**: `/api/intents/search`
- **Method**: `GET`
- **Description**: Search for intents based on various criteria.
- **Parameters**:
  - `query`: Natural language search term.
  - `service_name`: Filter by service name.
  - `intent_name`: Filter by intent name.
  - `uid`: Filter by intent UID.
  - `namespace`: Filter by namespace.
  - `description`: Filter by description.
  - `tags`: Filter by tags.

**Example Request**:

```curl
GET /api/intents/search?intent_name=SearchProducts
```

**Example Response**:

```json
{
  "intents": [
    {
      "service_name": "E-commerce Platform",
      "intent_name": "SearchProducts",
      "intent_uid": "ecommerce.com:SearchProducts:v1",
      "description": "Search for products based on criteria",
      "input_parameters": [
        {"name": "query", "type": "string", "required": true}
      ],
      "output_parameters": [
        {"name": "products", "type": "array", "description": "List of products"}
      ],
      "endpoint": "https://api.ecommerce.com/products/search",
      "tags": ["e-commerce", "search", "products"]
    }
  ]
}
```

## Execution API

The Execution API allows AI agents to execute intents on web services.

### Endpoints

#### Execute Intent

- **Endpoint**: `/api/intents/execute`
- **Method**: `POST`
- **Description**: Execute an intent with the provided parameters.
- **Headers**:
  - `Authorization`: Bearer PAT-12345
  - `Content-Type`: application/json

**Example Request**:

```json
POST /api/intents/execute
Authorization: Bearer PAT-12345
Content-Type: application/json

{
  "intent_uid": "ecommerce.com:SearchProducts:v1",
  "parameters": {
    "query": "laptops"
  }
}
```

**Example Response**:

```json
{
  "products": [
    {
      "product_id": "123",
      "name": "Gaming Laptop",
      "price": 1500
    },
    {
      "product_id": "124",
      "name": "Ultrabook",
      "price": 1200
    }
  ],
  "total_results": 2
}
```

## Policy API

The Policy API allows AI agents to retrieve policies and request Policy Adherence Tokens (PATs) from web services.

### Endpoints

#### Get Policy

- **Endpoint**: `/api/policy`
- **Method**: `GET`
- **Description**: Retrieve the ODRL policy for the service.

**Example Response**:

```json
{
  "@context": "http://www.w3.org/ns/odrl.jsonld",
  "uid": "http://example.com/policy/12345",
  "type": "Set",
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
      ]
    }
  ]
}
```

#### Request PAT

- **Endpoint**: `/api/policy/pat`
- **Method**: `POST`
- **Description**: Request a Policy Adherence Token (PAT) after agreeing to the policy.
- **Headers**:
  - `Content-Type`: application/json

**Example Request**:

```json
POST /api/policy/pat
Content-Type: application/json

{
  "policy_uid": "http://example.com/policy/12345",
  "agent_id": "ai-agent-1",
  "agent_public_key": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQE...",
  "signature": "Base64-encoded-digital-signature"
}
```

**Example Response**:

```json
{
  "pat": {
    "uid": "pat-12345",
    "issued_to": "ai-agent-1",
    "issued_by": "example.com",
    "policy_reference": "http://example.com/policy/12345",
    "permissions": ["execute:intent/SearchProducts"],
    "valid_from": "2024-01-01T00:00:00Z",
    "valid_to": "2024-12-31T23:59:59Z"
  },
  "signature": "Base64-encoded-digital-signature"
}
```

## Error Handling

All APIs follow a standard error response format:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Descriptive error message.",
    "details": {
      "additional": "context-specific information"
    }
  }
}
```

For a complete list of error codes and messages, see the [Error Codes](../specification/uim-specification.md#a-standard-error-codes-and-messages) section in the main specification.

## API Versioning

The UIM Protocol APIs are versioned to ensure backward compatibility. The version is included in the URL path:

```
/api/v1/intents/search
```

## Authentication

Most API endpoints require authentication using a Policy Adherence Token (PAT). The PAT is included in the `Authorization` header:

```
Authorization: Bearer PAT-12345
```

## Rate Limiting

API endpoints may enforce rate limits as specified in the policy. Rate limit information is included in the response headers:

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1609459200
```

## Further Reading

For more detailed information about the UIM Protocol APIs, refer to the [main specification](../specification/uim-specification.md).
