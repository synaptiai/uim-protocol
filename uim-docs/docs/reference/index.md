# UIM Protocol Technical Reference

Welcome to the UIM Protocol Technical Reference. This section provides detailed technical information about the protocol, including vocabulary, schemas, and error codes.

## Reference Documentation

- [ODRL Vocabulary](odrl-vocabulary.md): Detailed documentation of the Open Digital Rights Language (ODRL) vocabulary used in the UIM Protocol
- [Licensing Scheme](licensing-scheme.md): Information about the UIM Licensing Scheme for defining permissions, conditions, and prohibitions
- [Error Codes](error-codes.md): Comprehensive list of error codes and their meanings
- [JSON Schemas](json-schemas.md): JSON Schema definitions for all data structures used in the protocol

## Data Models

The UIM Protocol defines several key data models:

### Intent

```json
{
  "intent_uid": "example.com:search-products:v1",
  "intent_name": "SearchProducts",
  "description": "Search for products based on criteria",
  "input_parameters": [
    {"name": "query", "type": "string", "required": true, "description": "Search term"},
    {"name": "category", "type": "string", "required": false, "description": "Product category"},
    {"name": "price_range", "type": "string", "required": false, "description": "Price range filter"},
    {"name": "sort_by", "type": "string", "required": false, "description": "Sorting criteria"}
  ],
  "output_parameters": [
    {"name": "products", "type": "array", "description": "List of products"},
    {"name": "total_results", "type": "integer", "description": "Total number of results"}
  ],
  "endpoint": "https://api.example.com/products/search",
  "tags": ["e-commerce", "search", "products"]
}
```

### Policy Adherence Token (PAT)

```json
{
  "pat": {
    "uid": "pat-12345",
    "issued_to": "ai-agent-1",
    "issued_by": "example.com",
    "policy_reference": "http://example.com/policy/12345",
    "permissions": ["execute:intent/SearchProducts"],
    "obligations": ["pay:0.01 USD per intent"],
    "billing_info": {
      "payment_method": "credit_card",
      "billing_address": "123 AI Street, Tech City",
      "currency": "USD"
    },
    "valid_from": "2024-01-01T00:00:00Z",
    "valid_to": "2024-12-31T23:59:59Z"
  },
  "signature": "Base64-encoded-digital-signature"
}
```

### Service Description

```json
{
  "service": {
    "name": "Example Service",
    "description": "Service description",
    "version": "1.0.0",
    "urls": {
      "service": "https://api.example.com",
      "terms": "https://example.com/terms",
      "privacy": "https://example.com/privacy",
      "documentation": "https://example.com/docs"
    }
  },
  "intents": [
    {
      "uid": "example.com:intent-name:v1",
      "name": "IntentName",
      "description": "Intent description",
      "endpoint": {
        "url": "https://api.example.com/endpoint",
        "method": "POST"
      }
    }
  ],
  "security": {
    "public_key": "base64-encoded-public-key",
    "policy_url": "https://example.com/policy.json",
    "supported_auth_methods": [
      "jwt",
      "oauth2"
    ]
  },
  "compliance": {
    "standards": [
      "ISO27001",
      "GDPR"
    ],
    "certifications": [
      "SOC2"
    ]
  }
}
```

## API Reference

For detailed API reference documentation, please see the [API Guidelines](../specification/api-guidelines.md) section of the specification.

## Tools and Libraries

We're developing tools and libraries to help you implement the UIM Protocol:

- **UIM Validator**: A tool for validating UIM Protocol implementations
- **UIM Client Library**: A client library for implementing UIM Protocol in AI agents
- **UIM Server Library**: A server library for implementing UIM Protocol in web services

These tools and libraries are currently in development and will be available soon.
