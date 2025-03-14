# Implementation Guide based on UIM Mock Agent and Mock Web Service

This guide will walk you through the setup and usage of the UIM Mock Agent and Mock Web Service. The UIM Mock Agent simulates an AI agent interacting with a mock web service according to the Unified Intent Mediator (UIM) specification. It demonstrates the discovery and execution of intents, issuance of Policy Adherence Tokens (PATs), policy retrieval and signing, and secure key management for multiple web services. 

By following the steps outlined, you can simulate the discovery and execution of intents, manage keys, retrieve and sign policies, and handle PAT issuance. This setup demonstrates the core functionalities of the Unified Intent Mediator (UIM) specification in a mock environment.

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Setup

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/synaptiai/uim-protocol.git
cd uim-mock-webservice
```

### 2. Install Dependencies

Install the required dependencies for both the mock agent and the mock web service:

```bash
pip install -r requirements.txt
```

### 3. Running the Mock Web Service

The mock web service is implemented using FastAPI and provides endpoints for discovering intents, retrieving policies, issuing PATs, and executing intents.

#### Start the Web Service

Run the web service using Uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 4000
```

This will start the web service on [http://localhost:4000](http://localhost:4000).
Keep this running in a separate terminal window.

#### Web Service Endpoints

The FastAPI framework provides automatic interactive documentation for the web service endpoints. You can access it by navigating to [http://localhost:4000/docs](http://localhost:4000/docs). This will open a Swagger UI page with the available endpoints and their documentation. The following endpoints are available:

- GET /agents.json: Returns the available intents and service information.
- GET /uim-policy.json: Returns the ODRL policy for the service.
- POST /pat/issue: Issues a PAT after verifying the signed policy.
- POST /uim/execute: Executes an intent using the provided parameters and PAT.

### 4. Running the Mock Agent

The mock agent is a command-line interface (CLI) application that interacts with the mock web service. It allows you to manage keys, discover intents, view policies, sign policies, get PATs, and execute intents.

#### Start the Mock Agent CLI

Navigate to the uim-mock-agent directory and run the CLI interface:

```bash
cd uim-mock-agent
python src/cli_interface.py
```

#### CLI Menu Options

The CLI provides the following options:

- Manage Keys: Generate new key pairs or view existing key pairs for a service.
- Discover Intents: Fetch and display available intents from the web service.
- View Policy: Retrieve and display the ODRL policy from the web service.
- Sign Policy and Get PAT: Sign the policy and request a PAT from the web service.
- Execute Intent: Execute an intent using the provided parameters and PAT.
- Exit: Exit the CLI.

## Detailed Usage

### 1. Manage Keys

This option allows you to generate new RSA key pairs or view existing key pairs for a service URL.

- Generate new key pair: Creates a new RSA key pair and saves it under the keys/ directory.
- View existing key pair: Displays the private and public keys for the specified service URL.
- Set current service URL: Sets the service URL for subsequent operations.

### 2. Discover Intents

Fetches the agents.json from the web service and displays the available intents along with their descriptions and input parameters.

### 3. View Policy

Fetches the uim-policy.json from the web service and displays the ODRL policy, including permissions, prohibitions, parties, and assets.

### 4. Sign Policy and Get PAT

- Fetch Policy: Retrieves the ODRL policy from the web service.
- Sign Policy: Signs the policy using the agent's private key.
- Get PAT: Submits the signed policy to the web service and requests a PAT. The PAT is used for authenticating subsequent intent executions.

### 5. Execute Intent

- Enter Intent UID: Specify the UID of the intent to execute.
- Enter Parameters: Provide the required parameters for the intent.
- Execute: Sends a request to the web service to execute the intent using the provided parameters and PAT.

### Example Workflow

- Start the Web Service:

```bash
cd uim-mock-webservice
uvicorn main:app --host 0.0.0.0 --port 4000
```

- Start the Mock Agent CLI:

```bash
cd uim-mock-agent
python src/cli_interface.py
```

- Set Current Service URL:
  - Select "Manage Keys" (Option 1)
  - Select "Set current service URL" (Option 3)
  - Enter [http://localhost:4000](http://localhost:4000)
- Generate Key Pair:
  - Select "Manage Keys" (Option 1)
  - Select "Generate new key pair" (Option 1)
- Discover Intents:
  - Select "Discover Intents" (Option 2)
- View Policy:
  - Select "View Policy" (Option 3)
- Sign Policy and Get PAT:
  - Select "Sign Policy and Get PAT" (Option 4)
  - Enter your agent ID when prompted
- Execute Intent:
  - Select "Execute Intent" (Option 5)
  - Enter the intent UID (e.g., fakerealestate.com:searchProperty:v1)
  - Enter the required parameters (e.g., location, min_price, max_price, property_type)
