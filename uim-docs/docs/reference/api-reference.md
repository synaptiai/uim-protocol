# API Reference

This section provides a comprehensive reference for the UIM Protocol APIs, including detailed specifications for all endpoints, request and response formats, and error codes.

## Discovery API

The Discovery API allows AI agents to discover available intents and services.

### Intent Search

Searches for available intents based on given criteria.

**Endpoint**: `/api/intents/search`
**Method**: GET
**Content-Type**: application/json

#### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| query | string | No | The natural language query or search term |
| service_name | string | No | The name of a service |
| intent_name | string | No | The name of an intent |
| uid | string | No | The unique identifier of an intent |
| namespace | string | No | The namespace of a service |
| description | string | No | The description of an intent |
| tags | string | No | A comma-separated list of tags |
| page | integer | No | The page number for pagination (default: 1) |
| page_size | integer | No | The number of results per page (default: 10) |

#### Response

**Status Code**: 200 OK

```json
{
  "intents": [
    {
      "service_name": "E-commerce Platform",
      "intent_name": "SearchProducts",
      "intent_uid": "ecommerce.com:searchProducts:v1",
      "description": "Search for products based on given criteria",
      "input_parameters": [
        {"name": "query", "type": "string", "required": true},
        {"name": "category", "type": "string", "required": false},
        {"name": "price_range", "type": "string", "required": false},
        {"name": "sort_by", "type": "string", "required": false}
      ],
      "output_parameters": [
        {"name": "products", "type": "array", "required": true},
        {"name": "total_results", "type": "integer", "required": true}
      ],
      "endpoint": "https://api.ecommerce.com/products/search",
      "tags": ["e-commerce", "search", "products"]
    }
  ],
  "pagination": {
    "total_results": 1,
    "total_pages": 1,
    "current_page": 1,
    "page_size": 10
  }
}
```

#### Error Responses

| Status Code | Error Code | Description |
|-------------|------------|-------------|
| 400 | INVALID_PARAMETER | One or more parameters are invalid |
| 401 | UNAUTHORIZED | Authentication is required |
| 403 | FORBIDDEN | Access to this resource is forbidden |
| 500 | INTERNAL_SERVER_ERROR | An unexpected error occurred on the server |

### Intent Details

Retrieves detailed information about a specific intent.

**Endpoint**: `/api/intents/{intent_uid}`
**Method**: GET
**Content-Type**: application/json

#### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| intent_uid | string | Yes | The unique identifier of the intent |

#### Response

**Status Code**: 200 OK

```json
{
  "intent_uid": "ecommerce.com:searchProducts:v1",
  "service_name": "E-commerce Platform",
  "intent_name": "SearchProducts",
  "description": "Search for products based on given criteria",
  "input_parameters": [
    {"name": "query", "type": "string", "required": true},
    {"name": "category", "type": "string", "required": false},
    {"name": "price_range", "type": "string", "required": false},
    {"name": "sort_by", "type": "string", "required": false}
  ],
  "output_parameters": [
    {"name": "products", "type": "array", "required": true},
    {"name": "total_results", "type": "integer", "required": true}
  ],
  "endpoint": "https://api.ecommerce.com/products/search",
  "tags": ["e-commerce", "search", "products"]
}
```

#### Error Responses

| Status Code | Error Code | Description |
|-------------|------------|-------------|
| 400 | INVALID_PARAMETER | The intent_uid parameter is invalid |
| 401 | UNAUTHORIZED | Authentication is required |
| 403 | FORBIDDEN | Access to this resource is forbidden |
| 404 | NOT_FOUND | The intent was not found |
| 500 | INTERNAL_SERVER_ERROR | An unexpected error occurred on the server |

## Execution API

The Execution API allows AI agents to execute intents.

### Execute Intent

Executes an intent based on the provided input parameters.

**Endpoint**: `/api/intents/execute`
**Method**: POST
**Content-Type**: application/json
**Authorization**: Bearer \<PAT\>

#### Request Body

```json
{
  "intent_uid": "ecommerce.com:searchProducts:v1",
  "parameters": {
    "query": "laptops",
    "category": "electronics",
    "price_range": "1000-2000",
    "sort_by": "popularity"
  }
}
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| intent_uid | string | Yes | The unique identifier of the intent |
| parameters | object | Yes | The parameters required to execute the intent |

#### Response

**Status Code**: 200 OK

The response format depends on the intent being executed. For example, for the `searchProducts` intent:

```json
{
  "total_results": 2,
  "products": [
    {
      "product_id": "123",
      "name": "Gaming Laptop",
      "price": 1500,
      "category": "electronics"
    },
    {
      "product_id": "456",
      "name": "Business Laptop",
      "price": 1200,
      "category": "electronics"
    }
  ]
}
```

#### Error Responses

| Status Code | Error Code | Description |
|-------------|------------|-------------|
| 400 | INVALID_PARAMETER | One or more parameters are invalid |
| 401 | UNAUTHORIZED | Authentication is required or the PAT is invalid |
| 403 | FORBIDDEN | The PAT does not grant permission to execute this intent |
| 404 | NOT_FOUND | The intent was not found |
| 429 | TOO_MANY_REQUESTS | The rate limit has been exceeded |
| 500 | INTERNAL_SERVER_ERROR | An unexpected error occurred on the server |
| 503 | SERVICE_UNAVAILABLE | The service is temporarily unavailable |

## Policy API

The Policy API allows AI agents to retrieve policies and request Policy Adherence Tokens (PATs).

### Get Policy

Retrieves the policy for the service.

**Endpoint**: `/api/policy`
**Method**: GET
**Content-Type**: application/json

#### Response

**Status Code**: 200 OK

```json
{
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
  ],
  "prohibition": [
    {
      "target": "http://example.com/api/intents",
      "action": "exceedRateLimit"
    }
  ],
  "obligation": [
    {
      "action": "signPayload",
      "assignee": "http://example.com/ai-agent/1",
      "target": "http://example.com/vocab/payload",
      "constraint": [
        {
          "leftOperand": "http://example.com/vocab/publicKey",
          "operator": "use",
          "rightOperand": "MIIBIjANBgkqh..."
        }
      ]
    }
  ]
}
```

#### Error Responses

| Status Code | Error Code | Description |
|-------------|------------|-------------|
| 500 | INTERNAL_SERVER_ERROR | An unexpected error occurred on the server |

### Request PAT

Requests a Policy Adherence Token (PAT) for the service.

**Endpoint**: `/api/pat/issue`
**Method**: POST
**Content-Type**: application/json

#### Request Body

```json
{
  "agent_id": "ai-agent-123",
  "signed_policy": "base64-encoded-signature",
  "agent_public_key": "base64-encoded-public-key"
}
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| agent_id | string | Yes | The identifier for the AI agent |
| signed_policy | string | Yes | The policy signed by the AI agent |
| agent_public_key | string | Yes | The public key of the AI agent |

#### Response

**Status Code**: 200 OK

```json
{
  "uim-pat": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_at": "2023-12-31T23:59:59Z"
}
```

#### Error Responses

| Status Code | Error Code | Description |
|-------------|------------|-------------|
| 400 | INVALID_PARAMETER | One or more parameters are invalid |
| 400 | INVALID_SIGNATURE | The signature is invalid |
| 403 | POLICY_REJECTED | The policy was rejected |
| 500 | INTERNAL_SERVER_ERROR | An unexpected error occurred on the server |

## Service Management API

The Service Management API allows web services to register and manage their intents.

### Register Service

Registers a new service with the central repository.

**Endpoint**: `/api/services`
**Method**: POST
**Content-Type**: application/json
**Authorization**: Bearer \<Admin Token\>

#### Request Body

```json
{
  "service_name": "E-commerce Platform",
  "service_url": "https://api.ecommerce.com",
  "description": "Provides e-commerce functionalities",
  "policy_url": "https://api.ecommerce.com/policy",
  "service_logo_url": "https://api.ecommerce.com/logo.png",
  "service_terms_of_service_url": "https://api.ecommerce.com/terms",
  "service_privacy_policy_url": "https://api.ecommerce.com/privacy"
}
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| service_name | string | Yes | The name of the service |
| service_url | string | Yes | The URL of the service |
| description | string | Yes | A brief description of the service |
| policy_url | string | No | The policies URL of the service |
| service_logo_url | string | No | The URL of the service's logo |
| service_terms_of_service_url | string | No | The URL of the service's terms of service |
| service_privacy_policy_url | string | No | The URL of the service's privacy policy |

#### Response

**Status Code**: 201 Created

```json
{
  "service_id": "12345",
  "service_name": "E-commerce Platform",
  "service_url": "https://api.ecommerce.com",
  "description": "Provides e-commerce functionalities"
}
```

#### Error Responses

| Status Code | Error Code | Description |
|-------------|------------|-------------|
| 400 | INVALID_PARAMETER | One or more parameters are invalid |
| 401 | UNAUTHORIZED | Authentication is required |
| 403 | FORBIDDEN | Access to this resource is forbidden |
| 409 | CONFLICT | A service with the same name already exists |
| 500 | INTERNAL_SERVER_ERROR | An unexpected error occurred on the server |

### Update Service

Updates the details of an existing service.

**Endpoint**: `/api/services/{service_id}`
**Method**: PUT
**Content-Type**: application/json
**Authorization**: Bearer \<Admin Token\>

#### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| service_id | string | Yes | The identifier of the service |

#### Request Body

Same as Register Service.

#### Response

**Status Code**: 200 OK

```json
{
  "service_id": "12345",
  "service_name": "E-commerce Platform",
  "service_url": "https://api.ecommerce.com",
  "description": "Provides e-commerce functionalities"
}
```

#### Error Responses

| Status Code | Error Code | Description |
|-------------|------------|-------------|
| 400 | INVALID_PARAMETER | One or more parameters are invalid |
| 401 | UNAUTHORIZED | Authentication is required |
| 403 | FORBIDDEN | Access to this resource is forbidden |
| 404 | NOT_FOUND | The service was not found |
| 500 | INTERNAL_SERVER_ERROR | An unexpected error occurred on the server |

### Delete Service

Deletes a registered service.

**Endpoint**: `/api/services/{service_id}`
**Method**: DELETE
**Authorization**: Bearer \<Admin Token\>

#### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| service_id | string | Yes | The identifier of the service |

#### Response

**Status Code**: 204 No Content

#### Error Responses

| Status Code | Error Code | Description |
|-------------|------------|-------------|
| 401 | UNAUTHORIZED | Authentication is required |
| 403 | FORBIDDEN | Access to this resource is forbidden |
| 404 | NOT_FOUND | The service was not found |
| 500 | INTERNAL_SERVER_ERROR | An unexpected error occurred on the server |

### Retrieve Service

Retrieves the details of a registered service.

**Endpoint**: `/api/services/{service_id}`
**Method**: GET
**Content-Type**: application/json

#### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| service_id | string | Yes | The identifier of the service |

#### Response

**Status Code**: 200 OK

```json
{
  "service_id": "12345",
  "service_name": "E-commerce Platform",
  "service_url": "https://api.ecommerce.com",
  "description": "Provides e-commerce functionalities",
  "policy_url": "https://api.ecommerce.com/policy",
  "service_logo_url": "https://api.ecommerce.com/logo.png",
  "service_terms_of_service_url": "https://api.ecommerce.com/terms",
  "service_privacy_policy_url": "https://api.ecommerce.com/privacy"
}
```

#### Error Responses

| Status Code | Error Code | Description |
|-------------|------------|-------------|
| 401 | UNAUTHORIZED | Authentication is required |
| 403 | FORBIDDEN | Access to this resource is forbidden |
| 404 | NOT_FOUND | The service was not found |
| 500 | INTERNAL_SERVER_ERROR | An unexpected error occurred on the server |

## Intent Management API

The Intent Management API allows web services to manage their intents.

### List All Intents for a Service

Lists all intents for a specific service.

**Endpoint**: `/api/services/{service_id}/intents`
**Method**: GET
**Content-Type**: application/json

#### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| service_id | string | Yes | The identifier of the service |
| page | integer | No | The page number for pagination (default: 1) |
| page_size | integer | No | The number of results per page (default: 10) |

#### Response

**Status Code**: 200 OK

```json
{
  "intents": [
    {
      "intent_id": "67890",
      "intent_uid": "ecommerce.com:searchProducts:v1",
      "intent_name": "SearchProducts",
      "description": "Search for products based on given criteria",
      "tags": ["e-commerce", "search", "products"]
    }
  ],
  "pagination": {
    "total_results": 1,
    "total_pages": 1,
    "current_page": 1,
    "page_size": 10
  }
}
```

#### Error Responses

| Status Code | Error Code | Description |
|-------------|------------|-------------|
| 401 | UNAUTHORIZED | Authentication is required |
| 403 | FORBIDDEN | Access to this resource is forbidden |
| 404 | NOT_FOUND | The service was not found |
| 500 | INTERNAL_SERVER_ERROR | An unexpected error occurred on the server |

### Create Intent

Creates a new intent for a specific service.

**Endpoint**: `/api/services/{service_id}/intents`
**Method**: POST
**Content-Type**: application/json
**Authorization**: Bearer \<Admin Token\>

#### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| service_id | string | Yes | The identifier of the service |

#### Request Body

```json
{
  "intent_uid": "ecommerce.com:searchProducts:v1",
  "intent_name": "SearchProducts",
  "description": "Search for products based on given criteria",
  "input_parameters": [
    {"name": "query", "type": "string", "required": true},
    {"name": "category", "type": "string", "required": false},
    {"name": "price_range", "type": "string", "required": false},
    {"name": "sort_by", "type": "string", "required": false}
  ],
  "output_parameters": [
    {"name": "products", "type": "array", "required": true},
    {"name": "total_results", "type": "integer", "required": true}
  ],
  "endpoint": "https://api.ecommerce.com/products/search",
  "tags": ["e-commerce", "search", "products"]
}
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| intent_uid | string | Yes | The unique identifier for the intent |
| intent_name | string | Yes | The name of the intent |
| description | string | Yes | A brief description of what the intent does |
| input_parameters | array | Yes | An array of input parameters required by the intent |
| output_parameters | array | Yes | An array of output parameters returned by the intent |
| endpoint | string | Yes | The URL endpoint for the intent |
| tags | array | No | An array of tags associated with the intent |

#### Response

**Status Code**: 201 Created

```json
{
  "intent_id": "67890",
  "intent_uid": "ecommerce.com:searchProducts:v1",
  "intent_name": "SearchProducts",
  "description": "Search for products based on given criteria"
}
```

#### Error Responses

| Status Code | Error Code | Description |
|-------------|------------|-------------|
| 400 | INVALID_PARAMETER | One or more parameters are invalid |
| 401 | UNAUTHORIZED | Authentication is required |
| 403 | FORBIDDEN | Access to this resource is forbidden |
| 404 | NOT_FOUND | The service was not found |
| 409 | CONFLICT | An intent with the same UID already exists |
| 500 | INTERNAL_SERVER_ERROR | An unexpected error occurred on the server |

### Update Intent

Updates the details of an existing intent.

**Endpoint**: `/api/intents/{intent_id}`
**Method**: PUT
**Content-Type**: application/json
**Authorization**: Bearer \<Admin Token\>

#### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| intent_id | string | Yes | The identifier of the intent |

#### Request Body

Same as Create Intent.

#### Response

**Status Code**: 200 OK

```json
{
  "intent_id": "67890",
  "intent_uid": "ecommerce.com:searchProducts:v1",
  "intent_name": "SearchProducts",
  "description": "Search for products based on given criteria"
}
```

#### Error Responses

| Status Code | Error Code | Description |
|-------------|------------|-------------|
| 400 | INVALID_PARAMETER | One or more parameters are invalid |
| 401 | UNAUTHORIZED | Authentication is required |
| 403 | FORBIDDEN | Access to this resource is forbidden |
| 404 | NOT_FOUND | The intent was not found |
| 500 | INTERNAL_SERVER_ERROR | An unexpected error occurred on the server |

### Delete Intent

Deletes an existing intent.

**Endpoint**: `/api/intents/{intent_id}`
**Method**: DELETE
**Authorization**: Bearer \<Admin Token\>

#### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| intent_id | string | Yes | The identifier of the intent |

#### Response

**Status Code**: 204 No Content

#### Error Responses

| Status Code | Error Code | Description |
|-------------|------------|-------------|
| 401 | UNAUTHORIZED | Authentication is required |
| 403 | FORBIDDEN | Access to this resource is forbidden |
| 404 | NOT_FOUND | The intent was not found |
| 500 | INTERNAL_SERVER_ERROR | An unexpected error occurred on the server |

## Error Codes

The UIM Protocol defines the following error codes:

### Client-Side Errors (4xx)

| Error Code | Description | Example Scenario |
|------------|-------------|------------------|
| INVALID_PARAMETER | The request is missing a required parameter or contains an invalid parameter | A required field such as query in a search intent is not provided |
| UNAUTHORIZED | The request is not authenticated or the authentication token is invalid or expired | The AI agent attempts to access a service without providing a valid OAuth2.0 token |
| FORBIDDEN | The client is authenticated but does not have the necessary permissions to access the resource | An AI agent tries to execute an intent that it does not have permission to use |
| NOT_FOUND | The specified resource or endpoint could not be found on the server | The AI agent requests an intent or service that does not exist |
| METHOD_NOT_ALLOWED | The client attempted to use an HTTP method that is not supported by the endpoint | Sending a POST request to an endpoint that only supports GET |
| CONFLICT | The request could not be processed because of a conflict in the current state of the resource | Attempting to register an intent that already exists under a different version |
| UNSUPPORTED_MEDIA_TYPE | The server does not support the media type of the request payload | The client sends a request with an unsupported content type, such as text/xml instead of application/json |

### Server-Side Errors (5xx)

| Error Code | Description | Example Scenario |
|------------|-------------|------------------|
| INTERNAL_SERVER_ERROR | A generic error message when the server encounters an unexpected condition | The server encounters a null pointer exception or other unhandled error |
| SERVICE_UNAVAILABLE | The server is currently unable to handle the request due to maintenance or overload | The server is down for maintenance, or a service dependency is unavailable |
| GATEWAY_TIMEOUT | The server, while acting as a gateway, did not receive a response from an upstream server in time | A request to an external API exceeds the timeout limit |
| NOT_IMPLEMENTED | The server does not support the functionality required to fulfill the request | The AI agent attempts to use an intent that is not yet supported by the service |

### Protocol-Level Errors

| Error Code | Description | Example Scenario |
|------------|-------------|------------------|
| INTENT_EXECUTION_FAILED | The execution of an intent fails due to invalid input, missing parameters, or other issues | An AI agent tries to execute GetProductDetails but fails because the required product_id is missing |
| INTENT_NOT_SUPPORTED | The requested intent is not recognized or supported by the target service | An AI agent requests an intent that has been deprecated or is not implemented by the service |
| VERSION_CONFLICT | There is a conflict between the requested version of the intent and the version supported by the service | An AI agent attempts to execute version v1 of an intent when only v2 is supported |
| INTENT_DEPRECATED | The intent has been deprecated and is no longer available for use | The AI agent calls a deprecated intent that has been removed in the latest version of the protocol |
