# Mock Agent

The Mock Agent is a simulated AI agent that implements the Unified Intent Mediator (UIM) Protocol. It serves as a reference implementation and testing tool for developers working with the protocol.

## Overview

The Mock Agent demonstrates how AI agents can discover services, request Policy Adherence Tokens (PATs), and execute intents using the UIM Protocol. It provides a command-line interface for interacting with UIM-compatible web services.

## Features

- **Service Discovery**: Discovers web services using DNS TXT records and `agents.json` files.
- **Intent Discovery**: Searches for intents based on various criteria.
- **Policy Retrieval**: Retrieves and parses policies from web services.
- **Policy Signing**: Signs policies using RSA key pairs.
- **PAT Acquisition**: Requests and manages PATs from web services.
- **Intent Execution**: Executes intents with the appropriate parameters and PATs.
- **Command-Line Interface**: Provides a user-friendly CLI for interacting with the agent.

## Architecture

The Mock Agent is built with a modular architecture that separates concerns and promotes maintainability:

```
+------------------+
|     CLI Layer    |
+------------------+
         |
+------------------+
|   Agent Core     |
+------------------+
         |
+------------------+     +------------------+     +------------------+
| Discovery Module |     |  Policy Module   |     | Execution Module |
+------------------+     +------------------+     +------------------+
         |                       |                        |
+------------------+     +------------------+     +------------------+
| Network Layer    |     | Crypto Layer     |     | Storage Layer    |
+------------------+     +------------------+     +------------------+
```

### Components

1. **CLI Layer**: Provides the command-line interface for users to interact with the agent.
2. **Agent Core**: Coordinates the different modules and manages the agent's state.
3. **Discovery Module**: Handles service and intent discovery.
4. **Policy Module**: Manages policy retrieval, parsing, and signing.
5. **Execution Module**: Handles intent execution and result processing.
6. **Network Layer**: Manages HTTP requests and responses.
7. **Crypto Layer**: Handles cryptographic operations like key generation and signing.
8. **Storage Layer**: Manages persistent storage of keys, PATs, and other data.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/synaptiai/uim-protocol.git
   cd uim-protocol/src/uim-mock-agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Generate keys (if not already present):
   ```bash
   python mock_agent.py generate-keys
   ```

## Usage

### Basic Commands

The Mock Agent provides several commands for interacting with UIM-compatible web services:

#### Discover a Service

```bash
python mock_agent.py discover --domain example.com
```

This command will:
1. Look up DNS TXT records for `example.com`
2. Fetch the `agents.json` file
3. Parse and display service information

#### Search for Intents

```bash
python mock_agent.py search-intents --service-url https://api.example.com --tags e-commerce,search
```

This command will:
1. Query the service's discovery endpoint
2. Filter intents based on the provided tags
3. Display the matching intents

#### Get a PAT

```bash
python mock_agent.py get-pat --service-url https://api.example.com
```

This command will:
1. Retrieve the service's policy
2. Sign the policy with the agent's private key
3. Request a PAT from the service
4. Store the PAT for future use

#### Execute an Intent

```bash
python mock_agent.py execute --service-url https://api.example.com --intent-uid example.com:searchProducts:v1 --parameters '{"query": "laptop", "category": "electronics"}'
```

This command will:
1. Retrieve the PAT for the service (or request a new one if needed)
2. Execute the intent with the provided parameters
3. Display the result

### Advanced Usage

#### Interactive Mode

The Mock Agent also provides an interactive mode for more complex interactions:

```bash
python mock_agent.py interactive
```

This will start an interactive shell where you can enter commands and see the results in real-time.

#### Batch Mode

For automated testing, you can use batch mode to execute a series of commands from a file:

```bash
python mock_agent.py batch --file commands.txt
```

Where `commands.txt` contains one command per line.

#### Verbose Mode

To see more detailed information about what the agent is doing, use the `--verbose` flag:

```bash
python mock_agent.py discover --domain example.com --verbose
```

## Configuration

The Mock Agent can be configured using a configuration file or environment variables.

### Configuration File

Create a file named `config.json` in the agent's directory:

```json
{
  "agent_id": "mock-agent-123",
  "keys_dir": "./keys",
  "pats_dir": "./pats",
  "log_level": "INFO",
  "timeout": 30,
  "verify_ssl": true
}
```

### Environment Variables

You can also use environment variables to configure the agent:

- `UIM_AGENT_ID`: The identifier for the agent
- `UIM_KEYS_DIR`: Directory for storing keys
- `UIM_PATS_DIR`: Directory for storing PATs
- `UIM_LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR)
- `UIM_TIMEOUT`: Request timeout in seconds
- `UIM_VERIFY_SSL`: Whether to verify SSL certificates

## Extending the Mock Agent

The Mock Agent is designed to be extensible. Here are some ways you can extend it:

### Adding New Commands

To add a new command, create a new file in the `commands` directory:

```python
# commands/my_command.py
from .base import BaseCommand

class MyCommand(BaseCommand):
    name = "my-command"
    description = "Description of my command"

    def add_arguments(self, parser):
        parser.add_argument("--my-arg", help="Description of my argument")

    def execute(self, args):
        # Implementation of the command
        print(f"Executing my command with arg: {args.my_arg}")
```

Then register the command in `commands/__init__.py`.

### Adding New Modules

To add a new module, create a new file in the `modules` directory:

```python
# modules/my_module.py
class MyModule:
    def __init__(self, agent):
        self.agent = agent

    def my_function(self, arg):
        # Implementation of the function
        return f"Result: {arg}"
```

Then initialize the module in `agent.py`.

## Testing

The Mock Agent includes a comprehensive test suite to ensure its functionality:

```bash
pytest
```

For more detailed test output:

```bash
pytest -v
```

To run specific tests:

```bash
pytest tests/test_discovery.py
```

## Troubleshooting

### Common Issues

#### DNS Resolution Errors

If you're having trouble with DNS resolution:

1. Check that the domain exists and has TXT records
2. Try using the `--dns-server` flag to specify a different DNS server
3. Use the `--verbose` flag to see more detailed error information

#### PAT Acquisition Errors

If you're having trouble acquiring PATs:

1. Check that your keys are generated correctly
2. Verify that the service's policy is accessible
3. Ensure that your agent ID is valid
4. Use the `--verbose` flag to see more detailed error information

#### Intent Execution Errors

If you're having trouble executing intents:

1. Check that you have a valid PAT for the service
2. Verify that the intent UID is correct
3. Ensure that the parameters are valid for the intent
4. Use the `--verbose` flag to see more detailed error information

### Logging

The Mock Agent logs information to the console and to a log file. To change the log level:

```bash
python mock_agent.py --log-level DEBUG discover --domain example.com
```

Log files are stored in the `logs` directory.

## Contributing

We welcome contributions to the Mock Agent! Please see the [Contributing Guide](../community/contributing.md) for more information.

## License

The Mock Agent is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/synaptiai/uim-protocol/blob/main/LICENSE) file for details.
