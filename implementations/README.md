# UIM Protocol Reference Implementations

This directory contains reference implementations of the Unified Intent Mediator (UIM) Protocol components. These implementations serve as practical examples and starting points for developers looking to integrate the UIM Protocol into their systems.

## Available Implementations

### Centralized Discovery Service

The `centralized-discovery-service` directory contains a reference implementation of a centralized discovery service for the UIM Protocol. This service allows AI agents to discover available intents from registered web services.

**Key Features:**
- Intent registration and management
- Intent discovery API
- Service registration and management
- Policy management

**Technologies:**
- Python with FastAPI
- PostgreSQL for data storage
- Docker for containerization

### UIM Mock Agent

The `uim-mock-agent` directory contains a reference implementation of an AI agent that can interact with web services using the UIM Protocol.

**Key Features:**
- Intent discovery
- Policy agreement
- Intent execution
- PAT management

**Technologies:**
- Python
- Command-line interface

### UIM Mock Web Service

The `uim-mock-webservice` directory contains a reference implementation of a web service that exposes intents using the UIM Protocol.

**Key Features:**
- Intent definition and exposure
- Policy definition
- PAT issuance
- Intent execution

**Technologies:**
- Python with FastAPI
- Docker for containerization

## Getting Started

Each implementation directory contains its own README.md file with specific instructions for setting up and running the implementation. Generally, you'll need to:

1. Install the required dependencies
2. Configure the environment variables
3. Run the implementation

## Contributing

If you'd like to contribute to these reference implementations, please follow the [contribution guidelines](../CONTRIBUTING.md). We welcome improvements, bug fixes, and additional implementations to showcase different aspects of the UIM Protocol.

## License

All reference implementations are licensed under the Apache License 2.0 - see the [LICENSE](../LICENSE) file for details.
