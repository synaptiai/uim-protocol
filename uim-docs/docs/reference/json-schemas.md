# JSON Schemas

This page provides JSON Schema definitions for all data structures used in the UIM Protocol. These schemas can be used to validate requests and responses, generate client libraries, and document APIs.

## Introduction to JSON Schema

JSON Schema is a vocabulary that allows you to annotate and validate JSON documents. The UIM Protocol uses JSON Schema to define the structure of its data models, ensuring consistency and interoperability between implementations.

## Core Schemas

### Intent Schema

The Intent Schema defines the structure of an intent, including its metadata, parameters, and endpoint.

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

### Policy Schema

The Policy Schema defines the structure of a policy, including permissions, prohibitions, and obligations.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Policy",
  "description": "A UIM Protocol policy",
  "type": "object",
  "required": [
    "@context",
    "uid",
    "type"
  ],
  "properties": {
    "@context": {
      "type": "string",
      "description": "The JSON-LD context for the policy",
      "enum": [
        "http://www.w3.org/ns/odrl.jsonld"
      ]
    },
    "uid": {
      "type": "string",
      "description": "The unique identifier for the policy",
      "format": "uri"
    },
    "type": {
      "type": "string",
      "description": "The type of the policy",
      "enum": [
        "Set",
        "Offer",
        "Agreement"
      ]
    },
    "profile": {
      "type": "string",
      "description": "The profile for the policy",
      "format": "uri"
    },
    "permission": {
      "type": "array",
      "description": "The permissions for the policy",
      "items": {
        "$ref": "#/definitions/permission"
      }
    },
    "prohibition": {
      "type": "array",
      "description": "The prohibitions for the policy",
      "items": {
        "$ref": "#/definitions/prohibition"
      }
    },
    "obligation": {
      "type": "array",
      "description": "The obligations for the policy",
      "items": {
        "$ref": "#/definitions/obligation"
      }
    }
  },
  "definitions": {
    "permission": {
      "type": "object",
      "required": [
        "target",
        "action"
      ],
      "properties": {
        "target": {
          "type": "string",
          "description": "The target of the permission",
          "format": "uri"
        },
        "action": {
          "type": "string",
          "description": "The action of the permission"
        },
        "constraint": {
          "type": "array",
          "description": "The constraints for the permission",
          "items": {
            "$ref": "#/definitions/constraint"
          }
        },
        "duty": {
          "type": "array",
          "description": "The duties for the permission",
          "items": {
            "$ref": "#/definitions/duty"
          }
        }
      }
    },
    "prohibition": {
      "type": "object",
      "required": [
        "target",
        "action"
      ],
      "properties": {
        "target": {
          "type": "string",
          "description": "The target of the prohibition",
          "format": "uri"
        },
        "action": {
          "type": "string",
          "description": "The action of the prohibition"
        },
        "constraint": {
          "type": "array",
          "description": "The constraints for the prohibition",
          "items": {
            "$ref": "#/definitions/constraint"
          }
        }
      }
    },
    "obligation": {
      "type": "object",
      "required": [
        "action"
      ],
      "properties": {
        "action": {
          "type": "string",
          "description": "The action of the obligation"
        },
        "assignee": {
          "type": "string",
          "description": "The assignee of the obligation",
          "format": "uri"
        },
        "target": {
          "type": "string",
          "description": "The target of the obligation",
          "format": "uri"
        },
        "constraint": {
          "type": "array",
          "description": "The constraints for the obligation",
          "items": {
            "$ref": "#/definitions/constraint"
          }
        }
      }
    },
    "constraint": {
      "type": "object",
      "required": [
        "leftOperand",
        "operator",
        "rightOperand"
      ],
      "properties": {
        "leftOperand": {
          "type": "string",
          "description": "The left operand of the constraint",
          "format": "uri"
        },
        "operator": {
          "type": "string",
          "description": "The operator of the constraint",
          "enum": [
            "eq",
            "neq",
            "gt",
            "gte",
            "lt",
            "lte",
            "within",
            "use"
          ]
        },
        "rightOperand": {
          "description": "The right operand of the constraint"
        },
        "unit": {
          "type": "string",
          "description": "The unit of the constraint",
          "format": "uri"
        }
      }
    },
    "duty": {
      "type": "object",
      "required": [
        "action"
      ],
      "properties": {
        "action": {
          "type": "string",
          "description": "The action of the duty"
        },
        "target": {
          "type": "string",
          "description": "The target of the duty",
          "format": "uri"
        },
        "amount": {
          "type": ["number", "object"],
          "description": "The amount of the duty"
        },
        "unit": {
          "type": "string",
          "description": "The unit of the duty",
          "format": "uri"
        },
        "timeInterval": {
          "type": "string",
          "description": "The time interval of the duty",
          "pattern": "^P([0-9]+Y)?([0-9]+M)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+S)?)?$"
        }
      }
    }
  }
}
```

### PAT Schema

The PAT Schema defines the structure of a Policy Adherence Token (PAT).

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "PAT",
  "description": "A UIM Protocol Policy Adherence Token (PAT)",
  "type": "object",
  "required": [
    "iss",
    "sub",
    "exp",
    "nbf",
    "jti",
    "scope",
    "pol"
  ],
  "properties": {
    "iss": {
      "type": "string",
      "description": "The issuer of the PAT"
    },
    "sub": {
      "type": "string",
      "description": "The subject of the PAT"
    },
    "exp": {
      "type": "integer",
      "description": "The expiration time of the PAT",
      "format": "unix-time"
    },
    "nbf": {
      "type": "integer",
      "description": "The not-before time of the PAT",
      "format": "unix-time"
    },
    "jti": {
      "type": "string",
      "description": "The JWT ID of the PAT"
    },
    "scope": {
      "type": "array",
      "description": "The scope of the PAT",
      "items": {
        "type": "string"
      }
    },
    "pol": {
      "type": "string",
      "description": "The policy reference of the PAT",
      "format": "uri"
    },
    "lmt": {
      "type": "object",
      "description": "The rate limit of the PAT",
      "required": [
        "rate",
        "period"
      ],
      "properties": {
        "rate": {
          "type": "integer",
          "description": "The rate limit",
          "minimum": 1
        },
        "period": {
          "type": "integer",
          "description": "The period in seconds",
          "minimum": 1
        }
      }
    },
    "bil": {
      "type": "object",
      "description": "The billing information of the PAT",
      "required": [
        "method",
        "id"
      ],
      "properties": {
        "method": {
          "type": "string",
          "description": "The billing method",
          "enum": [
            "credit_card",
            "invoice",
            "paypal",
            "stripe",
            "other"
          ]
        },
        "id": {
          "type": "string",
          "description": "The billing ID"
        }
      }
    }
  }
}
```

### Service Description Schema

The Service Description Schema defines the structure of a service description, including service information, intents, and security information.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Service Description",
  "description": "A UIM Protocol service description",
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
    },
    "uim-license": {
      "type": "string",
      "description": "The UIM license for the service, following the UIM Licensing Scheme format",
      "format": "uri"
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
          "type": "string",
          "description": "The endpoint for the intent",
          "format": "uri"
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

## API Schemas

### Intent Search Request Schema

The Intent Search Request Schema defines the structure of an intent search request.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Intent Search Request",
  "description": "A UIM Protocol intent search request",
  "type": "object",
  "properties": {
    "query": {
      "type": "string",
      "description": "The natural language query or search term"
    },
    "service_name": {
      "type": "string",
      "description": "The name of a service"
    },
    "intent_name": {
      "type": "string",
      "description": "The name of an intent"
    },
    "uid": {
      "type": "string",
      "description": "The unique identifier of an intent"
    },
    "namespace": {
      "type": "string",
      "description": "The namespace of a service"
    },
    "description": {
      "type": "string",
      "description": "The description of an intent"
    },
    "tags": {
      "type": "string",
      "description": "A comma-separated list of tags"
    },
    "page": {
      "type": "integer",
      "description": "The page number for pagination",
      "minimum": 1,
      "default": 1
    },
    "page_size": {
      "type": "integer",
      "description": "The number of results per page",
      "minimum": 1,
      "maximum": 100,
      "default": 10
    }
  }
}
```

### Intent Search Response Schema

The Intent Search Response Schema defines the structure of an intent search response.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Intent Search Response",
  "description": "A UIM Protocol intent search response",
  "type": "object",
  "required": [
    "intents",
    "pagination"
  ],
  "properties": {
    "intents": {
      "type": "array",
      "description": "The intents matching the search criteria",
      "items": {
        "$ref": "#/definitions/intent"
      }
    },
    "pagination": {
      "type": "object",
      "description": "Pagination information",
      "required": [
        "total_results",
        "total_pages",
        "current_page",
        "page_size"
      ],
      "properties": {
        "total_results": {
          "type": "integer",
          "description": "The total number of results",
          "minimum": 0
        },
        "total_pages": {
          "type": "integer",
          "description": "The total number of pages",
          "minimum": 0
        },
        "current_page": {
          "type": "integer",
          "description": "The current page number",
          "minimum": 1
        },
        "page_size": {
          "type": "integer",
          "description": "The number of results per page",
          "minimum": 1
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
          "type": "string",
          "description": "The endpoint for the intent",
          "format": "uri"
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

### Intent Execution Request Schema

The Intent Execution Request Schema defines the structure of an intent execution request.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Intent Execution Request",
  "description": "A UIM Protocol intent execution request",
  "type": "object",
  "required": [
    "intent_uid",
    "parameters"
  ],
  "properties": {
    "intent_uid": {
      "type": "string",
      "description": "The unique identifier of the intent",
      "pattern": "^[a-zA-Z0-9.-]+:[a-z0-9-]+:v[0-9]+(\\.[0-9]+)*$"
    },
    "parameters": {
      "type": "object",
      "description": "The parameters for the intent execution"
    }
  }
}
```

### PAT Request Schema

The PAT Request Schema defines the structure of a PAT request.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "PAT Request",
  "description": "A UIM Protocol PAT request",
  "type": "object",
  "required": [
    "agent_id",
    "signed_policy",
    "agent_public_key"
  ],
  "properties": {
    "agent_id": {
      "type": "string",
      "description": "The identifier for the AI agent"
    },
    "signed_policy": {
      "type": "string",
      "description": "The policy signed by the AI agent"
    },
    "agent_public_key": {
      "type": "string",
      "description": "The public key of the AI agent"
    }
  }
}
```

### PAT Response Schema

The PAT Response Schema defines the structure of a PAT response.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "PAT Response",
  "description": "A UIM Protocol PAT response",
  "type": "object",
  "required": [
    "uim-pat"
  ],
  "properties": {
    "uim-pat": {
      "type": "string",
      "description": "The Policy Adherence Token (PAT)"
    },
    "expires_at": {
      "type": "string",
      "description": "The expiration time of the PAT",
      "format": "date-time"
    }
  }
}
```

### Error Response Schema

The Error Response Schema defines the structure of an error response.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Error Response",
  "description": "A UIM Protocol error response",
  "type": "object",
  "required": [
    "error"
  ],
  "properties": {
    "error": {
      "type": "object",
      "required": [
        "code",
        "message"
      ],
      "properties": {
        "code": {
          "type": "string",
          "description": "The error code",
          "pattern": "^UIM-[A-Z]{3}-[0-9]{3}$"
        },
        "message": {
          "type": "string",
          "description": "The error message"
        },
        "details": {
          "type": "object",
          "description": "Additional details about the error"
        },
        "help_url": {
          "type": "string",
          "description": "A URL pointing to documentation about the error",
          "format": "uri"
        }
      }
    }
  }
}
```

## Using JSON Schemas

### Validation

You can use these JSON Schemas to validate requests and responses in your UIM Protocol implementation. Here's an example using the `ajv` library in JavaScript:

```javascript
const Ajv = require('ajv');
const ajv = new Ajv();

// Load the schema
const intentSchema = require('./schemas/intent.json');

// Compile the schema
const validate = ajv.compile(intentSchema);

// Validate an intent
const intent = {
  intent_uid: 'example.com:search-products:v1',
  intent_name: 'SearchProducts',
  description: 'Search for products based on criteria',
  input_parameters: [
    {
      name: 'query',
      type: 'string',
      required: true,
      description: 'Search query'
    }
  ],
  output_parameters: [
    {
      name: 'products',
      type: 'array',
      description: 'List of matching products'
    }
  ],
  endpoint: {
    url: 'https://api.example.com/products/search',
    method: 'POST',
    content_type: 'application/json'
  },
  tags: ['e-commerce', 'search', 'products']
};

const valid = validate(intent);
if (!valid) {
  console.error('Intent validation failed:', validate.errors);
} else {
  console.log('Intent validation succeeded');
}
```

### Code Generation

You can use these JSON Schemas to generate client libraries for your UIM Protocol implementation. Here's an example using the `openapi-generator` tool:

```bash
# Generate a TypeScript client
openapi-generator generate -i openapi.yaml -g typescript-fetch -o ./client

# Generate a Python client
openapi-generator generate -i openapi.yaml -g python -o ./client
```

### Documentation

You can use these JSON Schemas to generate documentation for your UIM Protocol implementation. Here's an example using the `redoc` tool:

```bash
# Generate HTML documentation
npx redoc-cli bundle openapi.yaml -o ./docs/index.html
```

## References

- [JSON Schema](https://json-schema.org/)
- [Understanding JSON Schema](https://json-schema.org/understanding-json-schema/)
- [JSON Schema Validator](https://www.jsonschemavalidator.net/)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
