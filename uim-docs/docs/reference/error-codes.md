# Error Codes

This page provides a comprehensive reference for error codes used in the UIM Protocol. These error codes are returned by web services when an error occurs during intent execution or other operations.

## Error Code Format

UIM Protocol error codes follow a standardized format:

```
UIM-[CATEGORY]-[CODE]
```

Where:
- `UIM` is the prefix for all UIM Protocol error codes
- `CATEGORY` is a three-letter code indicating the error category
- `CODE` is a three-digit number uniquely identifying the error within its category

For example, `UIM-AUT-001` indicates an authentication error with code 001.

## Error Response Format

When an error occurs, web services should return a response with the following structure:

```json
{
  "error": {
    "code": "UIM-AUT-001",
    "message": "Invalid authentication token",
    "details": {
      "reason": "The token has expired",
      "expiry": "2025-01-01T00:00:00Z"
    },
    "help_url": "https://example.com/docs/errors/UIM-AUT-001"
  }
}
```

Where:
- `code` is the error code
- `message` is a human-readable error message
- `details` is an optional object containing additional information about the error
- `help_url` is an optional URL pointing to documentation about the error

## Error Categories

### Authentication Errors (AUT)

Authentication errors occur when there are issues with the authentication process.

| Code | Name | Description | HTTP Status |
|------|------|-------------|-------------|
| UIM-AUT-001 | INVALID_TOKEN | The authentication token is invalid | 401 |
| UIM-AUT-002 | EXPIRED_TOKEN | The authentication token has expired | 401 |
| UIM-AUT-003 | MISSING_TOKEN | The authentication token is missing | 401 |
| UIM-AUT-004 | INVALID_SIGNATURE | The signature is invalid | 401 |
| UIM-AUT-005 | INVALID_CREDENTIALS | The credentials are invalid | 401 |
| UIM-AUT-006 | ACCOUNT_LOCKED | The account is locked | 401 |
| UIM-AUT-007 | ACCOUNT_DISABLED | The account is disabled | 401 |
| UIM-AUT-008 | INVALID_CLIENT | The client is invalid | 401 |
| UIM-AUT-009 | INVALID_GRANT | The grant is invalid | 401 |
| UIM-AUT-010 | UNSUPPORTED_GRANT_TYPE | The grant type is not supported | 400 |

### Authorization Errors (AUZ)

Authorization errors occur when there are issues with the authorization process.

| Code | Name | Description | HTTP Status |
|------|------|-------------|-------------|
| UIM-AUZ-001 | INSUFFICIENT_PERMISSIONS | The client does not have sufficient permissions | 403 |
| UIM-AUZ-002 | SCOPE_EXCEEDED | The requested scope exceeds the granted scope | 403 |
| UIM-AUZ-003 | INTENT_NOT_ALLOWED | The intent is not allowed for this client | 403 |
| UIM-AUZ-004 | RATE_LIMIT_EXCEEDED | The rate limit has been exceeded | 429 |
| UIM-AUZ-005 | QUOTA_EXCEEDED | The quota has been exceeded | 429 |
| UIM-AUZ-006 | BILLING_REQUIRED | Billing information is required | 402 |
| UIM-AUZ-007 | PAYMENT_REQUIRED | Payment is required | 402 |
| UIM-AUZ-008 | SUBSCRIPTION_EXPIRED | The subscription has expired | 402 |
| UIM-AUZ-009 | GEOGRAPHIC_RESTRICTION | The request is restricted in this geographic region | 403 |
| UIM-AUZ-010 | TIME_RESTRICTION | The request is restricted at this time | 403 |

### Validation Errors (VAL)

Validation errors occur when there are issues with the request parameters.

| Code | Name | Description | HTTP Status |
|------|------|-------------|-------------|
| UIM-VAL-001 | MISSING_PARAMETER | A required parameter is missing | 400 |
| UIM-VAL-002 | INVALID_PARAMETER | A parameter is invalid | 400 |
| UIM-VAL-003 | INVALID_FORMAT | The request format is invalid | 400 |
| UIM-VAL-004 | INVALID_CONTENT_TYPE | The content type is invalid | 415 |
| UIM-VAL-005 | INVALID_ACCEPT_TYPE | The accept type is invalid | 406 |
| UIM-VAL-006 | PARAMETER_TOO_LONG | A parameter is too long | 400 |
| UIM-VAL-007 | PARAMETER_TOO_SHORT | A parameter is too short | 400 |
| UIM-VAL-008 | PARAMETER_OUT_OF_RANGE | A parameter is out of range | 400 |
| UIM-VAL-009 | INVALID_ENUM_VALUE | An enum value is invalid | 400 |
| UIM-VAL-010 | INVALID_DATE_FORMAT | A date format is invalid | 400 |

### Resource Errors (RES)

Resource errors occur when there are issues with the requested resources.

| Code | Name | Description | HTTP Status |
|------|------|-------------|-------------|
| UIM-RES-001 | RESOURCE_NOT_FOUND | The requested resource was not found | 404 |
| UIM-RES-002 | RESOURCE_ALREADY_EXISTS | The resource already exists | 409 |
| UIM-RES-003 | RESOURCE_GONE | The resource is no longer available | 410 |
| UIM-RES-004 | RESOURCE_LOCKED | The resource is locked | 423 |
| UIM-RES-005 | RESOURCE_TOO_LARGE | The resource is too large | 413 |
| UIM-RES-006 | RESOURCE_MODIFIED | The resource has been modified | 412 |
| UIM-RES-007 | RESOURCE_CONFLICT | There is a conflict with the resource | 409 |
| UIM-RES-008 | RESOURCE_TEMPORARILY_UNAVAILABLE | The resource is temporarily unavailable | 503 |
| UIM-RES-009 | RESOURCE_PERMANENTLY_UNAVAILABLE | The resource is permanently unavailable | 410 |
| UIM-RES-010 | RESOURCE_LIMIT_EXCEEDED | The resource limit has been exceeded | 429 |

### Intent Errors (INT)

Intent errors occur when there are issues with intent execution.

| Code | Name | Description | HTTP Status |
|------|------|-------------|-------------|
| UIM-INT-001 | INTENT_NOT_FOUND | The requested intent was not found | 404 |
| UIM-INT-002 | INTENT_EXECUTION_FAILED | The intent execution failed | 500 |
| UIM-INT-003 | INTENT_TIMEOUT | The intent execution timed out | 504 |
| UIM-INT-004 | INTENT_CANCELLED | The intent execution was cancelled | 499 |
| UIM-INT-005 | INTENT_ALREADY_EXECUTED | The intent has already been executed | 409 |
| UIM-INT-006 | INTENT_DEPENDENCY_FAILED | A dependency of the intent failed | 424 |
| UIM-INT-007 | INTENT_PRECONDITION_FAILED | A precondition for the intent failed | 412 |
| UIM-INT-008 | INTENT_UNSUPPORTED | The intent is not supported | 501 |
| UIM-INT-009 | INTENT_DEPRECATED | The intent is deprecated | 410 |
| UIM-INT-010 | INTENT_VERSION_MISMATCH | The intent version does not match | 400 |

### Policy Errors (POL)

Policy errors occur when there are issues with policies.

| Code | Name | Description | HTTP Status |
|------|------|-------------|-------------|
| UIM-POL-001 | POLICY_NOT_FOUND | The requested policy was not found | 404 |
| UIM-POL-002 | POLICY_VIOLATION | The request violates a policy | 403 |
| UIM-POL-003 | POLICY_REJECTED | The policy was rejected | 403 |
| UIM-POL-004 | POLICY_EXPIRED | The policy has expired | 403 |
| UIM-POL-005 | POLICY_NOT_APPLICABLE | The policy is not applicable | 403 |
| UIM-POL-006 | POLICY_CONFLICT | There is a conflict between policies | 409 |
| UIM-POL-007 | POLICY_REQUIRES_AGREEMENT | The policy requires explicit agreement | 403 |
| UIM-POL-008 | POLICY_REQUIRES_PAYMENT | The policy requires payment | 402 |
| UIM-POL-009 | POLICY_REQUIRES_SUBSCRIPTION | The policy requires a subscription | 402 |
| UIM-POL-010 | POLICY_REQUIRES_VERIFICATION | The policy requires verification | 403 |

### Server Errors (SRV)

Server errors occur when there are issues with the server.

| Code | Name | Description | HTTP Status |
|------|------|-------------|-------------|
| UIM-SRV-001 | INTERNAL_SERVER_ERROR | An internal server error occurred | 500 |
| UIM-SRV-002 | SERVICE_UNAVAILABLE | The service is unavailable | 503 |
| UIM-SRV-003 | GATEWAY_TIMEOUT | The gateway timed out | 504 |
| UIM-SRV-004 | BAD_GATEWAY | The gateway is bad | 502 |
| UIM-SRV-005 | SERVER_OVERLOADED | The server is overloaded | 503 |
| UIM-SRV-006 | SERVER_MAINTENANCE | The server is undergoing maintenance | 503 |
| UIM-SRV-007 | DATABASE_ERROR | A database error occurred | 500 |
| UIM-SRV-008 | CACHE_ERROR | A cache error occurred | 500 |
| UIM-SRV-009 | NETWORK_ERROR | A network error occurred | 500 |
| UIM-SRV-010 | DEPENDENCY_ERROR | A dependency error occurred | 500 |

### Protocol Errors (PRO)

Protocol errors occur when there are issues with the protocol.

| Code | Name | Description | HTTP Status |
|------|------|-------------|-------------|
| UIM-PRO-001 | INVALID_REQUEST | The request is invalid | 400 |
| UIM-PRO-002 | METHOD_NOT_ALLOWED | The HTTP method is not allowed | 405 |
| UIM-PRO-003 | UNSUPPORTED_MEDIA_TYPE | The media type is not supported | 415 |
| UIM-PRO-004 | NOT_ACCEPTABLE | The requested representation is not acceptable | 406 |
| UIM-PRO-005 | TOO_MANY_REQUESTS | Too many requests have been made | 429 |
| UIM-PRO-006 | REQUEST_TIMEOUT | The request timed out | 408 |
| UIM-PRO-007 | REQUEST_ENTITY_TOO_LARGE | The request entity is too large | 413 |
| UIM-PRO-008 | REQUEST_URI_TOO_LONG | The request URI is too long | 414 |
| UIM-PRO-009 | PRECONDITION_FAILED | A precondition failed | 412 |
| UIM-PRO-010 | PROTOCOL_VERSION_NOT_SUPPORTED | The protocol version is not supported | 505 |

## Error Handling Best Practices

When handling errors in the UIM Protocol, follow these best practices:

1. **Use Appropriate Error Codes**: Use the most specific error code that applies to the situation.
2. **Provide Clear Error Messages**: Error messages should be clear, concise, and helpful.
3. **Include Relevant Details**: Include relevant details in the `details` field to help diagnose the issue.
4. **Use Appropriate HTTP Status Codes**: Use the HTTP status code that best matches the error.
5. **Provide Help URLs**: Include a `help_url` field pointing to documentation about the error.
6. **Log Errors**: Log errors on the server side for debugging and monitoring.
7. **Handle Errors Gracefully**: Clients should handle errors gracefully and provide appropriate feedback to users.
8. **Retry with Backoff**: For transient errors, clients should retry with exponential backoff.
9. **Validate Inputs**: Validate inputs before processing to catch errors early.
10. **Secure Error Messages**: Ensure error messages don't leak sensitive information.

## Error Handling Example

### Server-Side Error Handling

```javascript
function executeIntent(req, res) {
  try {
    // Validate request
    if (!req.body.intent_uid) {
      return res.status(400).json({
        error: {
          code: "UIM-VAL-001",
          message: "Missing required parameter: intent_uid",
          details: {
            parameter: "intent_uid"
          },
          help_url: "https://example.com/docs/errors/UIM-VAL-001"
        }
      });
    }
    
    // Check authentication
    if (!req.headers.authorization) {
      return res.status(401).json({
        error: {
          code: "UIM-AUT-003",
          message: "Missing authentication token",
          help_url: "https://example.com/docs/errors/UIM-AUT-003"
        }
      });
    }
    
    // Execute intent
    const result = executeIntentLogic(req.body.intent_uid, req.body.parameters);
    
    // Return result
    return res.status(200).json(result);
  } catch (error) {
    // Handle unexpected errors
    console.error("Intent execution error:", error);
    return res.status(500).json({
      error: {
        code: "UIM-INT-002",
        message: "Intent execution failed",
        details: {
          reason: error.message
        },
        help_url: "https://example.com/docs/errors/UIM-INT-002"
      }
    });
  }
}
```

### Client-Side Error Handling

```javascript
async function executeIntent(intentUid, parameters) {
  try {
    const response = await fetch("https://api.example.com/uim/execute", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${pat}`
      },
      body: JSON.stringify({
        intent_uid: intentUid,
        parameters: parameters
      })
    });
    
    const data = await response.json();
    
    if (!response.ok) {
      // Handle error
      if (data.error) {
        switch (data.error.code) {
          case "UIM-AUT-001":
          case "UIM-AUT-002":
            // Handle authentication errors
            refreshToken();
            break;
          case "UIM-AUZ-004":
            // Handle rate limiting
            await sleep(1000);
            return executeIntent(intentUid, parameters);
          case "UIM-INT-003":
            // Handle timeout
            return executeIntent(intentUid, parameters);
          default:
            // Handle other errors
            throw new Error(`${data.error.code}: ${data.error.message}`);
        }
      } else {
        throw new Error(`HTTP error: ${response.status}`);
      }
    }
    
    return data;
  } catch (error) {
    console.error("Error executing intent:", error);
    throw error;
  }
}
```

## References

- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [JSON API Errors](https://jsonapi.org/format/#errors)
- [OAuth 2.0 Error Codes](https://datatracker.ietf.org/doc/html/rfc6749#section-5.2)
- [UIM Protocol API Guidelines](../specification/api-guidelines.md)
