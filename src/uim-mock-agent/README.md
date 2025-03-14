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
- `requirements.txt`: Lists project dependencies
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

- Python 3.7 or higher
- pip (Python package manager)

### Quickstart

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd uim-mock-agent
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script:

   ```bash
   python src/cli_interface.py
   ```

This will demonstrate the discovery of intents and key management functionality. For other features, you can run the respective Python files in the `src` directory.
