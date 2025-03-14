# UIM Mock Agent

UIM Mock Agent is a Python-based application that simulates an AI agent interacting with a mock web service according to the Unified Intent Mediator (UIM) specification. It demonstrates the discovery and execution of intents, issuance of Policy Adherence Tokens (PATs), policy retrieval and signing, and secure key management for multiple web services.

## Overview

The UIM Mock Agent is designed with a modular architecture, separating concerns into distinct components:

- Discovery module for fetching and interpreting intent metadata
- Execution module for running intents
- Policy management for retrieving and signing ODRL policies
- Key management for generating and storing RSA key pairs
- Error handling module for centralized error management

Technologies used:

- Python 3.x
- requests library for HTTP interactions
- jwt for JSON Web Token handling
- cryptography for key pair generation and management
- pytest for testing (not implemented in the current state)

Project structure:

```txt
uim-mock-agent/
├── src/
│   ├── discovery.py
│   ├── intent_execution.py
│   ├── pat_issuance.py
│   ├── policy_management.py
│   ├── policy_signing.py
│   ├── key_management.py
│   ├── error_handling.py
│   └── cli_interface.py
├── keys/
│   └── {service_url}/
│       ├── private_key.pem
│       └── public_key.pem
└── README.md
```

## Features

- Discover available intents from a mock web service
- Execute intents with proper input handling
- Retrieve and sign ODRL policies for verification
- Generate and manage RSA key pairs for each web service
- Handle errors and provide clear feedback
- Command-line interface for user interaction

## Getting Started

### Requirements

- Python 3.10 or higher
- [Poetry](https://python-poetry.org/) for dependency management

### Quickstart

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
   cd implementations/uim-mock-agent
   ```

4. Run the main script with Poetry:

   ```bash
   # Activate the virtual environment
   poetry shell

   # Run the main script
   python src/cli_interface.py
   ```

   Or directly with Poetry:

   ```bash
   poetry run python implementations/uim-mock-agent/src/cli_interface.py
   ```

This will demonstrate the discovery of intents and key management functionality. For other features, you can run the respective Python files in the `src` directory.
