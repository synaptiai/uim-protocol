# API Guidelines

This section provides detailed guidelines for implementing the UIM Protocol APIs. These guidelines are designed to ensure consistency, reliability, and security across all implementations of the protocol.

## 1. General API Design Principles

When designing APIs for the UIM Protocol, follow these general principles:

### 1.1 RESTful Design

- Use HTTP methods appropriately:
  - **GET**: Retrieve resources
  - **POST**: Create resources or execute actions
  - **PUT**: Update resources
  - **DELETE**: Remove resources
- Use resource-oriented URLs
- Use HTTP status codes correctly
- Make APIs stateless

### 1.2 Consistency

- Use consistent naming conventions
- Use consistent parameter formats
- Use consistent error formats
- Use consistent response formats

### 1.3 Versioning

- Include version information in the URL (e.g., `/v1/intents`)
- Support multiple versions simultaneously during transitions
- Clearly document version differences and migration paths

### 1.4 Documentation

- Provide comprehensive API documentation
- Include examples for all endpoints
- Document all parameters, including their types, constraints, and whether they are required
- Document all possible error responses

## 2. API Endpoints

The UIM Protocol defines several key API endpoints that should be implemented by web services and discovery services. These endpoints are organized into the following categories:

### 2.1 Discovery Endpoints

#### 2.1.1 Intent Search

- **Endpoint**: `/api/intents/search`
- **Method**: GET
- **Description**: Searches for available intents based on given criteria.
- **Parameters**:
  - `query` (string, optional): The natural language query or search term.
  - `service_name` (string, optional): The name of a service.
  - `intent_name` (string, optional): The name of an intent.
  - `uid` (string, optional): The unique identifier of an intent.
  - `namespace` (string, optional): The namespace of a service.
  - `description` (string, optional): The description of an intent.
  - `tags` (string, optional): A comma-separated list of tags.
  - `page` (integer, optional): The page number for pagination (default: 1).
  - `page_size` (integer, optional): The number of results per page (default: 10).

**Example Request:**

```http
GET /api/intents/search?intent_name=SearchProducts&tags=e-commerce,search
```

**Example Response:**

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

#### 2.1.2 Intent Details

- **Endpoint**: `/api/intents/{intent_uid}`
- **Method**: GET
- **Description**: Retrieves detailed information about a specific intent.
- **Parameters**: None.

**Example Request:**

```http
GET /api/intents/ecommerce.com:searchProducts:v1
```

**Example Response:**

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

### 2.2 Execution Endpoints

#### 2.2.1 Execute Intent

- **Endpoint**: `/api/intents/execute`
- **Method**: POST
- **Description**: Executes an intent based on the provided input parameters.
- **Parameters**:
  - `intent_uid` (string, required): The identifier for the intent.
  - `parameters` (object, required): The parameters required to execute the intent.

**Example Request:**

```http
POST /api/intents/execute
Content-Type: application/json
Authorization: Bearer <PAT>

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

**Example Response:**

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

### 2.3 Policy Endpoints

#### 2.3.1 Get Policy

- **Endpoint**: `/api/policy`
- **Method**: GET
- **Description**: Retrieves the policy for the service.
- **Parameters**: None.

**Example Request:**

```http
GET /api/policy
```

**Example Response:**

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

#### 2.3.2 Request PAT

- **Endpoint**: `/api/pat/issue`
- **Method**: POST
- **Description**: Requests a Policy Adherence Token (PAT) for the service.
- **Parameters**:
  - `agent_id` (string, required): The identifier for the AI agent.
  - `signed_policy` (string, required): The policy signed by the AI agent.
  - `agent_public_key` (string, required): The public key of the AI agent.

**Example Request:**

```http
POST /api/pat/issue
Content-Type: application/json

{
  "agent_id": "ai-agent-123",
  "signed_policy": "base64-encoded-signature",
  "agent_public_key": "base64-encoded-public-key"
}
```

**Example Response:**

```json
{
  "uim-pat": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_at": "2023-12-31T23:59:59Z"
}
```

### 2.4 Service Management Endpoints

#### 2.4.1 Register Service

- **Endpoint**: `/api/services`
- **Method**: POST
- **Description**: Registers a new service with the central repository.
- **Parameters**:
  - `service_name` (string, required): The name of the service.
  - `service_url` (string, required): The URL of the service.
  - `description` (string, required): A brief description of the service.
  - `policy_url` (string, optional): The policies URL of the service.
  - `service_logo_url` (string, optional): The URL of the service's logo.
  - `service_terms_of_service_url` (string, optional): The URL of the service's terms of service.
  - `service_privacy_policy_url` (string, optional): The URL of the service's privacy policy.

**Example Request:**

```http
POST /api/services
Content-Type: application/json

{
  "service_name": "E-commerce Platform",
  "service_url": "https://api.ecommerce.com",
  "description": "Provides e-commerce functionalities"
}
```

**Example Response:**

```json
{
  "service_id": "12345",
  "service_name": "E-commerce Platform",
  "service_url": "https://api.ecommerce.com",
  "description": "Provides e-commerce functionalities"
}
```

#### 2.4.2 Update Service

- **Endpoint**: `/api/services/{service_id}`
- **Method**: PUT
- **Description**: Updates the details of an existing service.
- **Parameters**: Same as Register Service.

#### 2.4.3 Delete Service

- **Endpoint**: `/api/services/{service_id}`
- **Method**: DELETE
- **Description**: Deletes a registered service.
- **Parameters**: None.

#### 2.4.4 Retrieve Service

- **Endpoint**: `/api/services/{service_id}`
- **Method**: GET
- **Description**: Retrieves the details of a registered service.
- **Parameters**: None.

### 2.5 Intent Management Endpoints

#### 2.5.1 List All Intents for a Service

- **Endpoint**: `/api/services/{service_id}/intents`
- **Method**: GET
- **Description**: Lists all intents for a specific service.
- **Parameters**:
  - `page` (integer, optional): The page number for pagination (default: 1).
  - `page_size` (integer, optional): The number of results per page (default: 10).

#### 2.5.2 Create Intent

- **Endpoint**: `/api/services/{service_id}/intents`
- **Method**: POST
- **Description**: Creates a new intent for a specific service.
- **Parameters**:
  - `intent_uid` (string, required): The unique identifier for the intent.
  - `intent_name` (string, required): The name of the intent.
  - `description` (string, required): A brief description of what the intent does.
  - `input_parameters` (array of objects, required): An array of input parameters required by the intent.
  - `output_parameters` (array of objects, required): An array of output parameters returned by the intent.
  - `endpoint` (string, required): The URL endpoint for the intent.
  - `tags` (array of strings, optional): An array of tags associated with the intent.

#### 2.5.3 Update Intent

- **Endpoint**: `/api/intents/{intent_id}`
- **Method**: PUT
- **Description**: Updates the details of an existing intent.
- **Parameters**: Same as Create Intent.

#### 2.5.4 Delete Intent

- **Endpoint**: `/api/intents/{intent_id}`
- **Method**: DELETE
- **Description**: Deletes an existing intent.
- **Parameters**: None.

## 3. Pagination

To handle large sets of data efficiently and improve performance, it's essential to implement pagination for list endpoints. Pagination allows clients to request specific subsets of data, making it easier to manage and process responses.

### 3.1 Pagination Parameters

1. **page**: The page number to retrieve (integer, optional, default: 1).
2. **page_size**: The number of items to include on each page (integer, optional, default: 10).

### 3.2 Pagination Headers

In addition to the pagination parameters, the API should include pagination-related headers in the response to provide clients with information about the total number of items and pages available.

1. **X-Total-Count**: The total number of items available.
2. **X-Total-Pages**: The total number of pages available.
3. **X-Current-Page**: The current page number.
4. **X-Page-Size**: The number of items per page.

### 3.3 Pagination Response Format

The response body should include a `pagination` object with the following properties:

```json
{
  "pagination": {
    "total_results": 100,
    "total_pages": 10,
    "current_page": 1,
    "page_size": 10
  },
  "results": [
    // Array of items
  ]
}
```

## 4. Error Handling

Proper error handling is crucial for providing a good developer experience and helping clients troubleshoot issues. The UIM Protocol defines a standard error response format and a set of error codes to ensure consistency across implementations.

### 4.1 Error Response Format

All error responses should follow this format:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Descriptive error message",
    "details": {
      "additional": "context-specific information"
    }
  }
}
```

### 4.2 HTTP Status Codes

Use appropriate HTTP status codes to indicate the type of error:

- **400 Bad Request**: The request was malformed or contained invalid parameters.
- **401 Unauthorized**: The request requires authentication.
- **403 Forbidden**: The client does not have permission to access the requested resource.
- **404 Not Found**: The requested resource was not found.
- **405 Method Not Allowed**: The HTTP method is not supported for the requested resource.
- **409 Conflict**: The request could not be completed due to a conflict with the current state of the resource.
- **429 Too Many Requests**: The client has sent too many requests in a given amount of time.
- **500 Internal Server Error**: An unexpected error occurred on the server.
- **503 Service Unavailable**: The server is currently unable to handle the request.

### 4.3 Error Codes

The UIM Protocol defines the following error codes:

#### 4.3.1 Client-Side Errors (4xx)

| Error Code | Message | Description | Example Scenario |
| :---- | :---- | :---- | :---- |
| INVALID_PARAMETER | "The parameter '{param}' is required." | The request is missing a required parameter or contains an invalid parameter. | A required field such as query in a search intent is not provided. |
| UNAUTHORIZED | "Unauthorized access. Authentication is required." | The request is not authenticated or the authentication token is invalid or expired. | The AI agent attempts to access a service without providing a valid OAuth2.0 token. |
| FORBIDDEN | "Access to this resource is forbidden." | The client is authenticated but does not have the necessary permissions to access the resource. | An AI agent tries to execute an intent that it does not have permission to use. |
| NOT_FOUND | "The requested resource '{resource}' was not found." | The specified resource or endpoint could not be found on the server. | The AI agent requests an intent or service that does not exist. |
| METHOD_NOT_ALLOWED | "The HTTP method '{method}' is not allowed for this endpoint." | The client attempted to use an HTTP method that is not supported by the endpoint. | Sending a POST request to an endpoint that only supports GET. |
| CONFLICT | "The request could not be completed due to a conflict." | The request could not be processed because of a conflict in the current state of the resource. | Attempting to register an intent that already exists under a different version. |
| UNSUPPORTED_MEDIA_TYPE | "The media type '{type}' is not supported." | The server does not support the media type of the request payload. | The client sends a request with an unsupported content type, such as text/xml instead of application/json. |

#### 4.3.2 Server-Side Errors (5xx)

| Error Code | Message | Description | Example Scenario |
| :---- | :---- | :---- | :---- |
| INTERNAL_SERVER_ERROR | "An unexpected error occurred on the server. Please try again later." | A generic error message when the server encounters an unexpected condition. | The server encounters a null pointer exception or other unhandled error. |
| SERVICE_UNAVAILABLE | "The service is temporarily unavailable. Please try again later." | The server is currently unable to handle the request due to maintenance or overload. | The server is down for maintenance, or a service dependency is unavailable. |
| GATEWAY_TIMEOUT | "The server did not receive a timely response from the upstream server." | The server, while acting as a gateway, did not receive a response from an upstream server in time. | A request to an external API exceeds the timeout limit. |
| NOT_IMPLEMENTED | "The requested functionality is not implemented." | The server does not support the functionality required to fulfill the request. | The AI agent attempts to use an intent that is not yet supported by the service. |

#### 4.3.3 Protocol-Level Errors

| Error Code | Message | Description | Example Scenario |
| :---- | :---- | :---- | :---- |
| INTENT_EXECUTION_FAILED | "The intent '{intent}' could not be executed due to {reason}." | The execution of an intent fails due to invalid input, missing parameters, or other issues. | An AI agent tries to execute GetProductDetails but fails because the required product_id is missing. |
| INTENT_NOT_SUPPORTED | "The intent '{intent}' is not supported by this service." | The requested intent is not recognized or supported by the target service. | An AI agent requests an intent that has been deprecated or is not implemented by the service. |
| VERSION_CONFLICT | "The intent version '{version}' is not supported." | There is a conflict between the requested version of the intent and the version supported by the service. | An AI agent attempts to execute version v1 of an intent when only v2 is supported. |
| INTENT_DEPRECATED | "The intent '{intent}' has been deprecated and is no longer supported." | The intent has been deprecated and is no longer available for use. | The AI agent calls a deprecated intent that has been removed in the latest version of the protocol. |

### 4.4 Error Handling Best Practices

- **Be Specific**: Provide clear, specific error messages that help the client understand what went wrong and how to fix it.
- **Include Context**: Include relevant context in the error details to help with debugging.
- **Don't Expose Sensitive Information**: Ensure that error messages don't expose sensitive information like stack traces, internal server details, or credentials.
- **Log Errors**: Log all errors on the server side for monitoring and debugging purposes.
- **Provide Actionable Feedback**: When possible, include suggestions for how to resolve the error.

## 5. Authentication and Authorization

The UIM Protocol uses Policy Adherence Tokens (PATs) for authentication and authorization. This section provides guidelines for implementing PAT-based authentication and authorization in your API.

### 5.1 PAT-Based Authentication

- **Token Format**: PATs are implemented as JSON Web Tokens (JWTs) and should be included in the `Authorization` header of API requests using the Bearer scheme.
- **Token Validation**: Validate the PAT's signature, expiration time, and other claims before processing the request.
- **Token Renewal**: Provide a mechanism for renewing PATs before they expire.
- **Token Revocation**: Implement a mechanism for revoking PATs if necessary.

### 5.2 Authorization

- **Scope-Based Authorization**: Use the `scope` claim in the PAT to determine what actions the client is authorized to perform.
- **Rate Limiting**: Implement rate limiting based on the `lmt` claim in the PAT.
- **Access Control**: Implement access control based on the client's identity and permissions.

### 5.3 Security Best Practices

- **Use HTTPS**: Always use HTTPS to encrypt communications between clients and servers.
- **Validate Input**: Validate all input to prevent injection attacks.
- **Implement Rate Limiting**: Implement rate limiting to prevent abuse.
- **Use Strong Cryptography**: Use strong cryptographic algorithms for signing and verifying PATs.
- **Implement Proper Error Handling**: Return appropriate error responses for authentication and authorization failures.

## 6. API Documentation

Good API documentation is essential for helping developers understand and use your API effectively. This section provides guidelines for documenting your UIM Protocol API.

### 6.1 Documentation Format

- **OpenAPI Specification**: Use the OpenAPI Specification (formerly known as Swagger) to document your API.
- **Markdown**: Use Markdown for additional documentation, such as guides and tutorials.
- **Code Examples**: Include code examples in multiple programming languages.

### 6.2 Documentation Content

- **API Overview**: Provide an overview of your API, including its purpose and key features.
- **Authentication**: Explain how to authenticate with your API.
- **Endpoints**: Document all endpoints, including their URLs, methods, parameters, and responses.
- **Error Handling**: Explain how errors are handled and what error codes to expect.
- **Rate Limiting**: Explain any rate limiting policies.
- **Versioning**: Explain your versioning strategy and how to use different versions of the API.
- **Examples**: Provide examples of common use cases.

### 6.3 Interactive Documentation

- **API Explorer**: Provide an interactive API explorer that allows developers to make requests to your API and see the responses.
- **Sandbox Environment**: Provide a sandbox environment for testing API calls without affecting production data.

## 7. Performance and Scalability

Designing APIs for performance and scalability is crucial for ensuring a good user experience and handling growth. This section provides guidelines for optimizing the performance and scalability of your UIM Protocol API.

### 7.1 Caching

- **Response Caching**: Use HTTP caching headers to enable client-side caching of responses.
- **Cache-Control**: Use the `Cache-Control` header to specify caching policies.
- **ETag**: Use the `ETag` header to enable conditional requests.
- **Last-Modified**: Use the `Last-Modified` header to enable conditional requests based on modification time.

### 7.2 Compression

- **GZIP Compression**: Enable GZIP compression for API responses to reduce bandwidth usage.
- **Content-Encoding**: Use the `Content-Encoding` header to indicate the compression method used.

### 7.3 Rate Limiting

- **Rate Limit Headers**: Include rate limit information in response headers.
- **X-RateLimit-Limit**: The maximum number of requests allowed in a time window.
- **X-RateLimit-Remaining**: The number of requests remaining in the current time window.
- **X-RateLimit-Reset**: The time when the current rate limit window resets.

### 7.4 Asynchronous Processing

- **Webhooks**: Use webhooks for asynchronous notifications.
- **Long-Running Operations**: Use asynchronous processing for long-running operations.
- **Status Endpoints**: Provide endpoints for checking the status of asynchronous operations.

### 7.5 Load Balancing

- **Horizontal Scaling**: Design your API to support horizontal scaling.
- **Stateless Design**: Make your API stateless to facilitate horizontal scaling.
- **Load Balancer**: Use a load balancer to distribute traffic across multiple instances.

## 8. Monitoring and Analytics

Monitoring and analytics are essential for understanding how your API is being used and identifying issues. This section provides guidelines for implementing monitoring and analytics for your UIM Protocol API.

### 8.1 Metrics to Monitor

- **Request Volume**: Track the number of requests to your API.
- **Response Time**: Monitor the time it takes to respond to requests.
- **Error Rate**: Track the rate of errors returned by your API.
- **Resource Usage**: Monitor CPU, memory, and disk usage.
- **Concurrent Connections**: Track the number of concurrent connections to your API.

### 8.2 Logging

- **Request Logging**: Log all requests to your API, including the request method, URL, headers, and body.
- **Response Logging**: Log all responses from your API, including the status code, headers, and body.
- **Error Logging**: Log all errors that occur in your API, including stack traces and context information.
- **Performance Logging**: Log performance metrics for each request, such as response time and resource usage.

### 8.3 Alerting

- **Error Rate Alerts**: Set up alerts for high error rates.
- **Response Time Alerts**: Set up alerts for slow response times.
- **Resource Usage Alerts**: Set up alerts for high resource usage.
- **Availability Alerts**: Set up alerts for API downtime.

### 8.4 Analytics

- **Usage Analytics**: Track how your API is being used, including which endpoints are most popular.
- **User Analytics**: Track which users are using your API and how they are using it.
- **Performance Analytics**: Track the performance of your API over time.
- **Error Analytics**: Track the most common errors and their causes.

## 9. Conclusion

Following these API guidelines will help ensure that your UIM Protocol implementation is consistent, reliable, and secure. By adhering to these guidelines, you'll provide a better experience for developers using your API and make it easier for AI agents to interact with your web service.

Remember that these guidelines are not exhaustive, and you should also follow general best practices for API design and implementation. As the UIM Protocol evolves, these guidelines may be updated to reflect new best practices and requirements.
