# Mock Webservice

The Mock Webservice is a simulated web service that implements the Unified Intent Mediator (UIM) Protocol. It serves as a reference implementation and testing tool for developers working with the protocol.

## Overview

The Mock Webservice demonstrates how web services can expose intents, issue Policy Adherence Tokens (PATs), and process intent execution requests using the UIM Protocol. It provides a complete implementation of the server-side components of the protocol.

## Features

- **Intent Definition**: Defines and exposes intents with their parameters and metadata.
- **Policy Definition**: Creates and serves policies that AI agents must adhere to.
- **Discovery Endpoints**: Provides endpoints for AI agents to discover intents.
- **PAT Issuance**: Issues PATs to AI agents that agree to adhere to policies.
- **Intent Execution**: Processes intent execution requests from AI agents.
- **Simulated Business Logic**: Includes simulated business logic for testing intent execution.
- **Web Interface**: Provides a web interface for monitoring and managing the service.

## Architecture

The Mock Webservice is built with a modular architecture that separates concerns and promotes maintainability:

```
+------------------+
|   Web Interface  |
+------------------+
         |
+------------------+
|    API Layer     |
+------------------+
         |
+------------------+     +------------------+     +------------------+
| Discovery Module |     |  Policy Module   |     | Execution Module |
+------------------+     +------------------+     +------------------+
         |                       |                        |
+------------------+     +------------------+     +------------------+
| Intent Registry  |     | Crypto Service   |     | Business Logic   |
+------------------+     +------------------+     +------------------+
         |                       |                        |
+------------------+
|  Data Storage    |
+------------------+
```

### Components

1. **Web Interface**: Provides a user interface for monitoring and managing the service.
2. **API Layer**: Handles HTTP requests and responses.
3. **Discovery Module**: Manages intent discovery and service information.
4. **Policy Module**: Handles policy definition, serving, and PAT issuance.
5. **Execution Module**: Processes intent execution requests.
6. **Intent Registry**: Stores and manages intent definitions.
7. **Crypto Service**: Handles cryptographic operations like key management and signature verification.
8. **Business Logic**: Implements the actual functionality behind intents.
9. **Data Storage**: Manages persistent storage of intents, policies, and other data.

## Installation

### Prerequisites

- Node.js 14 or higher
- npm (Node.js package manager)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/synaptiai/uim-protocol.git
   cd uim-protocol/src/uim-mock-webservice
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Generate keys (if not already present):
   ```bash
   npm run generate-keys
   ```

4. Configure the service (see Configuration section).

5. Start the service:
   ```bash
   npm start
   ```

## Configuration

The Mock Webservice can be configured using a configuration file or environment variables.

### Configuration File

Create a file named `config.json` in the service's directory:

```json
{
  "service": {
    "name": "Mock E-commerce Service",
    "description": "A mock e-commerce service for testing the UIM Protocol",
    "url": "http://localhost:3000",
    "logo_url": "http://localhost:3000/logo.png",
    "terms_url": "http://localhost:3000/terms",
    "privacy_url": "http://localhost:3000/privacy"
  },
  "server": {
    "port": 3000,
    "host": "localhost"
  },
  "keys": {
    "private_key_path": "./keys/private-key.pem",
    "public_key_path": "./keys/public-key.pem"
  },
  "policy": {
    "rate_limit": 1000,
    "rate_limit_period": "hour",
    "intent_price": 0.01,
    "currency": "USD"
  },
  "storage": {
    "type": "memory"
  },
  "logging": {
    "level": "info",
    "file": "./logs/service.log"
  }
}
```

### Environment Variables

You can also use environment variables to configure the service:

- `UIM_SERVICE_NAME`: The name of the service
- `UIM_SERVICE_DESCRIPTION`: A description of the service
- `UIM_SERVICE_URL`: The URL of the service
- `UIM_SERVER_PORT`: The port to run the server on
- `UIM_SERVER_HOST`: The host to run the server on
- `UIM_PRIVATE_KEY_PATH`: Path to the private key file
- `UIM_PUBLIC_KEY_PATH`: Path to the public key file
- `UIM_RATE_LIMIT`: Rate limit for intent execution
- `UIM_RATE_LIMIT_PERIOD`: Period for rate limiting (second, minute, hour, day)
- `UIM_INTENT_PRICE`: Price per intent execution
- `UIM_CURRENCY`: Currency for intent pricing
- `UIM_STORAGE_TYPE`: Type of storage (memory, file, mongodb)
- `UIM_LOG_LEVEL`: Logging level (debug, info, warn, error)
- `UIM_LOG_FILE`: Path to the log file

## Usage

### Accessing the Web Interface

Once the service is running, you can access the web interface at `http://localhost:3000` (or the URL you configured).

The web interface provides:

- A dashboard with service statistics
- A list of defined intents
- A log of intent executions
- Configuration options
- PAT management

### Defining Intents

Intents can be defined in the `intents.json` file or through the web interface.

#### Example Intent Definition

```json
{
  "intent_uid": "mock-ecommerce:searchProducts:v1",
  "intent_name": "SearchProducts",
  "description": "Search for products based on criteria",
  "input_parameters": [
    {
      "name": "query",
      "type": "string",
      "required": true,
      "description": "Search query"
    },
    {
      "name": "category",
      "type": "string",
      "required": false,
      "description": "Product category"
    },
    {
      "name": "price_range",
      "type": "string",
      "required": false,
      "description": "Price range (e.g., '10-100')"
    },
    {
      "name": "sort_by",
      "type": "string",
      "required": false,
      "description": "Sort criteria"
    }
  ],
  "output_parameters": [
    {
      "name": "products",
      "type": "array",
      "description": "List of matching products"
    },
    {
      "name": "total_results",
      "type": "integer",
      "description": "Total number of matching products"
    }
  ],
  "endpoint": "/api/products/search",
  "tags": ["e-commerce", "search", "products"]
}
```

### Implementing Business Logic

The business logic for intents is implemented in the `handlers` directory. Each intent has a corresponding handler file.

#### Example Handler

```javascript
// handlers/searchProducts.js
module.exports = async function searchProducts(parameters) {
  const { query, category, price_range, sort_by } = parameters;
  
  // In a real implementation, this would query a database
  // For the mock service, we return simulated data
  const products = [
    {
      id: '123',
      name: 'Laptop',
      price: 1500,
      category: 'electronics',
      description: 'A powerful laptop'
    },
    {
      id: '456',
      name: 'Smartphone',
      price: 800,
      category: 'electronics',
      description: 'A feature-rich smartphone'
    }
  ];
  
  // Filter by category if provided
  let filteredProducts = products;
  if (category) {
    filteredProducts = filteredProducts.filter(p => p.category === category);
  }
  
  // Filter by price range if provided
  if (price_range) {
    const [min, max] = price_range.split('-').map(Number);
    filteredProducts = filteredProducts.filter(p => p.price >= min && p.price <= max);
  }
  
  // Sort if sort_by is provided
  if (sort_by === 'price_asc') {
    filteredProducts.sort((a, b) => a.price - b.price);
  } else if (sort_by === 'price_desc') {
    filteredProducts.sort((a, b) => b.price - a.price);
  }
  
  return {
    products: filteredProducts,
    total_results: filteredProducts.length
  };
};
```

### API Endpoints

The Mock Webservice provides the following API endpoints:

#### Discovery Endpoints

- `GET /agents.json`: Returns the service information and intents
- `GET /uim/intents/search`: Searches for intents based on query parameters
- `GET /uim/intents/:intent_uid`: Returns details for a specific intent

#### Policy Endpoints

- `GET /uim-policy.json`: Returns the service's policy
- `POST /pat/issue`: Issues a PAT to an AI agent

#### Execution Endpoints

- `POST /uim/execute`: Executes an intent

## DNS Configuration

To enable DNS-based discovery, you need to configure TXT records for your domain:

```
uim-agents-file=http://localhost:3000/agents.json
uim-api-discovery=http://localhost:3000/uim/intents/search
uim-policy-file=http://localhost:3000/uim-policy.json
```

For local testing, you can use a hosts file entry:

```
127.0.0.1 mock-service.local
```

And then configure the TXT records in a local DNS server or use a service like dnsmasq.

## Extending the Mock Webservice

The Mock Webservice is designed to be extensible. Here are some ways you can extend it:

### Adding New Intents

To add a new intent:

1. Define the intent in `intents.json` or through the web interface
2. Create a handler file in the `handlers` directory
3. Implement the business logic for the intent

### Adding Storage Backends

The Mock Webservice supports different storage backends. To add a new one:

1. Create a new file in the `storage` directory
2. Implement the storage interface
3. Register the storage backend in `storage/index.js`

### Adding Authentication Methods

To add a new authentication method:

1. Create a new file in the `auth` directory
2. Implement the authentication interface
3. Register the authentication method in `auth/index.js`

## Testing

The Mock Webservice includes a comprehensive test suite to ensure its functionality:

```bash
npm test
```

For more detailed test output:

```bash
npm run test:verbose
```

To run specific tests:

```bash
npm test -- --grep "Intent Execution"
```

## Deployment

The Mock Webservice can be deployed in various environments:

### Docker

A Dockerfile is provided for containerized deployment:

```bash
docker build -t uim-mock-webservice .
docker run -p 3000:3000 uim-mock-webservice
```

### Docker Compose

A docker-compose.yml file is provided for multi-container deployment:

```bash
docker-compose up
```

### Cloud Deployment

Instructions for deploying to various cloud platforms are available in the `deployment` directory.

## Troubleshooting

### Common Issues

#### Server Won't Start

If the server won't start:

1. Check that the port is not already in use
2. Verify that the configuration file is valid
3. Ensure that the keys are generated correctly
4. Check the logs for error messages

#### PAT Issuance Errors

If PAT issuance is failing:

1. Check that the agent's signature is valid
2. Verify that the agent's public key is in the correct format
3. Ensure that the policy is being served correctly
4. Check the logs for error messages

#### Intent Execution Errors

If intent execution is failing:

1. Check that the PAT is valid and not expired
2. Verify that the intent UID is correct
3. Ensure that the parameters are valid for the intent
4. Check the handler implementation for errors
5. Check the logs for error messages

### Logging

The Mock Webservice logs information to the console and to a log file. To change the log level:

```bash
UIM_LOG_LEVEL=debug npm start
```

Log files are stored in the `logs` directory.

## Contributing

We welcome contributions to the Mock Webservice! Please see the [Contributing Guide](../community/contributing.md) for more information.

## License

The Mock Webservice is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/synaptiai/uim-protocol/blob/main/LICENSE) file for details.
