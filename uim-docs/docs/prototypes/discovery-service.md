# Discovery Service

The Discovery Service is a centralized implementation of the Unified Intent Mediator (UIM) Protocol's discovery mechanism. It allows AI agents to discover web services and their intents through a centralized registry.

## Overview

While the UIM Protocol supports decentralized discovery through DNS TXT records and `agents.json` files, a centralized discovery service can provide additional benefits such as search capabilities, curation, and analytics. The Discovery Service prototype demonstrates how such a centralized service can be implemented.

## Features

- **Service Registration**: Allows web services to register their intents and policies.
- **Intent Discovery**: Provides a search API for AI agents to discover intents.
- **Service Verification**: Verifies the authenticity of registered services.
- **Analytics**: Tracks usage patterns and provides insights.
- **Curation**: Curates high-quality services and intents.
- **Web Interface**: Provides a web interface for browsing and managing services and intents.
- **API**: Offers a comprehensive API for programmatic access.

## Architecture

The Discovery Service is built with a modular architecture that separates concerns and promotes maintainability:

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
| Registry Module  |     | Search Module    |     | Analytics Module |
+------------------+     +------------------+     +------------------+
         |                       |                        |
+------------------+     +------------------+     +------------------+
| Verification     |     | Curation         |     | Notification     |
| Module           |     | Module           |     | Module           |
+------------------+     +------------------+     +------------------+
         |                       |                        |
+------------------+
|  Data Storage    |
+------------------+
```

### Components

1. **Web Interface**: Provides a user interface for browsing and managing services and intents.
2. **API Layer**: Handles HTTP requests and responses.
3. **Registry Module**: Manages service and intent registration.
4. **Search Module**: Provides search capabilities for discovering services and intents.
5. **Analytics Module**: Tracks usage patterns and provides insights.
6. **Verification Module**: Verifies the authenticity of registered services.
7. **Curation Module**: Curates high-quality services and intents.
8. **Notification Module**: Sends notifications about new services and intents.
9. **Data Storage**: Manages persistent storage of services, intents, and other data.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- MongoDB (for production deployments)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/synaptiai/uim-protocol.git
   cd uim-protocol/src/centralized-discovery-service
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the service (see Configuration section).

5. Initialize the database:
   ```bash
   python manage.py init-db
   ```

6. Start the service:
   ```bash
   python manage.py runserver
   ```

## Configuration

The Discovery Service can be configured using a configuration file or environment variables.

### Configuration File

Create a file named `.env` in the service's directory:

```
# Server Configuration
HOST=localhost
PORT=5000
DEBUG=True

# Database Configuration
DB_TYPE=mongodb
DB_HOST=localhost
DB_PORT=27017
DB_NAME=uim_discovery
DB_USER=
DB_PASSWORD=

# Security Configuration
SECRET_KEY=your-secret-key
JWT_SECRET=your-jwt-secret
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin
ADMIN_EMAIL=admin@example.com

# Verification Configuration
VERIFY_SERVICES=True
VERIFICATION_TIMEOUT=30

# Curation Configuration
ENABLE_CURATION=True
AUTO_APPROVE_SERVICES=False

# Analytics Configuration
ENABLE_ANALYTICS=True
ANALYTICS_RETENTION_DAYS=90

# Notification Configuration
ENABLE_NOTIFICATIONS=True
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USER=user@example.com
SMTP_PASSWORD=your-smtp-password
NOTIFICATION_FROM=noreply@example.com
```

### Environment Variables

You can also use environment variables to configure the service. The environment variables have the same names as the keys in the `.env` file.

## Usage

### Accessing the Web Interface

Once the service is running, you can access the web interface at `http://localhost:5000` (or the URL you configured).

The web interface provides:

- A dashboard with service statistics
- A list of registered services and intents
- Search functionality
- Service and intent details
- Administration tools

### API Endpoints

The Discovery Service provides the following API endpoints:

#### Service Endpoints

- `GET /api/services`: Lists all registered services
- `GET /api/services/{service_id}`: Returns details for a specific service
- `POST /api/services`: Registers a new service
- `PUT /api/services/{service_id}`: Updates a service
- `DELETE /api/services/{service_id}`: Deletes a service

#### Intent Endpoints

- `GET /api/intents`: Lists all registered intents
- `GET /api/intents/{intent_id}`: Returns details for a specific intent
- `GET /api/intents/search`: Searches for intents based on query parameters
- `POST /api/intents`: Registers a new intent
- `PUT /api/intents/{intent_id}`: Updates an intent
- `DELETE /api/intents/{intent_id}`: Deletes an intent

#### Authentication Endpoints

- `POST /api/auth/login`: Authenticates a user and returns a JWT
- `POST /api/auth/register`: Registers a new user
- `POST /api/auth/refresh`: Refreshes a JWT
- `POST /api/auth/logout`: Logs out a user

#### Admin Endpoints

- `GET /api/admin/users`: Lists all users
- `GET /api/admin/analytics`: Returns analytics data
- `POST /api/admin/verify-service/{service_id}`: Verifies a service
- `POST /api/admin/curate-intent/{intent_id}`: Curates an intent

### Service Registration

Web services can register with the Discovery Service using the API or the web interface.

#### API Registration

```bash
curl -X POST http://localhost:5000/api/services \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-jwt-token" \
  -d '{
    "name": "E-commerce Service",
    "description": "A service for e-commerce operations",
    "url": "https://api.example.com",
    "logo_url": "https://example.com/logo.png",
    "terms_url": "https://example.com/terms",
    "privacy_url": "https://example.com/privacy",
    "policy_url": "https://example.com/uim-policy.json",
    "discovery_url": "https://api.example.com/uim/intents/search",
    "intents": [
      {
        "intent_uid": "example.com:searchProducts:v1",
        "intent_name": "SearchProducts",
        "description": "Search for products based on criteria",
        "input_parameters": [
          {"name": "query", "type": "string", "required": true},
          {"name": "category", "type": "string", "required": false},
          {"name": "price_range", "type": "string", "required": false},
          {"name": "sort_by", "type": "string", "required": false}
        ],
        "output_parameters": [
          {"name": "products", "type": "array"},
          {"name": "total_results", "type": "integer"}
        ],
        "endpoint": "https://api.example.com/products/search",
        "tags": ["e-commerce", "search", "products"]
      }
    ]
  }'
```

#### Web Interface Registration

1. Log in to the web interface
2. Navigate to the "Services" section
3. Click "Register New Service"
4. Fill out the service details
5. Add intents
6. Submit the registration

### Intent Discovery

AI agents can discover intents using the API or the web interface.

#### API Discovery

```bash
curl -X GET "http://localhost:5000/api/intents/search?query=product&tags=e-commerce,search"
```

This will return a list of intents that match the query and tags.

#### Web Interface Discovery

1. Navigate to the "Intents" section
2. Use the search bar to search for intents
3. Filter by tags, service, or other criteria
4. View intent details

## Deployment

The Discovery Service can be deployed in various environments:

### Docker

A Dockerfile is provided for containerized deployment:

```bash
docker build -t uim-discovery-service .
docker run -p 5000:5000 uim-discovery-service
```

### Docker Compose

A docker-compose.yml file is provided for multi-container deployment:

```bash
docker-compose up
```

### Cloud Deployment

Instructions for deploying to various cloud platforms are available in the `deployment` directory.

## Integration with UIM Protocol

The Discovery Service integrates with the UIM Protocol in the following ways:

### For Web Services

Web services can register their intents and policies with the Discovery Service, making them discoverable by AI agents.

### For AI Agents

AI agents can use the Discovery Service to find web services and intents that match their requirements.

### Complementary to Decentralized Discovery

The Discovery Service complements the decentralized discovery mechanism of the UIM Protocol. AI agents can use both methods to discover services and intents.

## Extending the Discovery Service

The Discovery Service is designed to be extensible. Here are some ways you can extend it:

### Adding New Features

To add a new feature:

1. Create a new module in the appropriate directory
2. Implement the feature
3. Register the module in the application

### Adding Storage Backends

The Discovery Service supports different storage backends. To add a new one:

1. Create a new file in the `storage` directory
2. Implement the storage interface
3. Register the storage backend in `storage/__init__.py`

### Adding Authentication Methods

To add a new authentication method:

1. Create a new file in the `auth` directory
2. Implement the authentication interface
3. Register the authentication method in `auth/__init__.py`

## Testing

The Discovery Service includes a comprehensive test suite to ensure its functionality:

```bash
pytest
```

For more detailed test output:

```bash
pytest -v
```

To run specific tests:

```bash
pytest tests/test_registry.py
```

## Troubleshooting

### Common Issues

#### Server Won't Start

If the server won't start:

1. Check that the port is not already in use
2. Verify that the configuration file is valid
3. Ensure that the database is running and accessible
4. Check the logs for error messages

#### Registration Errors

If service registration is failing:

1. Check that the service details are valid
2. Verify that the service URL is accessible
3. Ensure that the intents are properly formatted
4. Check the logs for error messages

#### Search Errors

If intent search is failing:

1. Check that the search parameters are valid
2. Verify that the database is running and accessible
3. Ensure that there are intents in the database
4. Check the logs for error messages

### Logging

The Discovery Service logs information to the console and to a log file. To change the log level:

```bash
export DEBUG=True
python manage.py runserver
```

Log files are stored in the `logs` directory.

## Contributing

We welcome contributions to the Discovery Service! Please see the [Contributing Guide](../community/contributing.md) for more information.

## License

The Discovery Service is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/synaptiai/uim-protocol/blob/main/LICENSE) file for details.
