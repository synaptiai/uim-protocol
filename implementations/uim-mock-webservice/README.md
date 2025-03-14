# UIM Mock Web Service

This is a mock implementation of a web service that exposes intents according to the Unified Intent Mediator (UIM) protocol. It demonstrates how web services can define intents, issue Policy Adherence Tokens (PATs), and handle intent execution requests from AI agents.

## Features

- Exposes sample intents for demonstration purposes
- Implements the UIM protocol's discovery and execution endpoints
- Handles policy retrieval and PAT issuance
- Manages cryptographic keys for secure interactions
- Provides a simple FastAPI-based implementation

## Project Structure

```
uim-mock-webservice/
├── __init__.py
├── main.py              # FastAPI application entry point
├── keys/                # Directory for cryptographic keys
│   ├── private_key.pem  # Service's private key
│   └── public_key.pem   # Service's public key
└── README.md
```

## Getting Started

### Requirements

- Python 3.10 or higher
- [Poetry](https://python-poetry.org/) for dependency management

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/synaptiai/uim-protocol.git
   cd uim-protocol
   ```

2. Install dependencies with Poetry:

   ```bash
   # Install Poetry if you haven't already
   curl -sSL https://install.python-poetry.org | python3 -

   # Install dependencies
   poetry install
   ```

3. Navigate to the implementation directory:

   ```bash
   cd implementations/uim-mock-webservice
   ```

4. Run the web service:

   ```bash
   # Activate the virtual environment
   poetry shell

   # Run the web service
   uvicorn main:app --reload
   ```

   Or directly with Poetry:

   ```bash
   poetry run uvicorn implementations/uim-mock-webservice/main:app --reload
   ```

5. Access the API documentation:

   Open your browser and navigate to `http://localhost:8000/docs` to see the Swagger UI documentation.

## API Endpoints

- **GET /agents.json**: Returns the agents.json file with service information and available intents
- **GET /policy**: Returns the ODRL policy for the service
- **POST /policy/pat**: Issues a Policy Adherence Token (PAT) after verifying the signed policy
- **POST /execute/{intent_name}**: Executes the specified intent with the provided parameters

## Testing with UIM Mock Agent

You can test this mock web service using the [UIM Mock Agent](../uim-mock-agent/README.md) implementation. The agent will discover the intents exposed by this service, request a PAT, and execute intents.

## License

This project is licensed under the Apache License 2.0.
