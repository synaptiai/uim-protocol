<div align="center">
  <img src="https://synaptiai.github.io/uim-protocol/assets/images/abstract.png" alt="UIM Protocol Logo">
  <h1>The Unified Intent Mediator Protocol</h1>
  <p>A standardized framework for AI agents to interact with web services through well-defined intents</p>
</div>

## Getting Started

1. Get familiar with the [concepts and motivations](https://synaptiai.github.io/uim-protocol/specification/) behind the UIM protocol
2. Explore the [prototype implementations](https://synaptiai.github.io/uim-protocol/prototypes/) to see the UIM protocol in action

## Development Setup

This project uses [Poetry](https://python-poetry.org/) for dependency management. Poetry provides a better way to manage Python dependencies with features like dependency resolution, virtual environments, and more.

### Prerequisites

- Python 3.10 or higher
- [Poetry](https://python-poetry.org/docs/#installation)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/synaptiai/uim-protocol.git
   cd uim-protocol
   ```

2. Install dependencies with Poetry:
   ```bash
   poetry install
   ```

   This will create a virtual environment and install all dependencies.

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

### Dependency Groups

The project uses Poetry's dependency groups to organize dependencies:

- **Main**: Core dependencies for the UIM Protocol
- **Dev**: Development dependencies (testing, linting, etc.)
- **Docs**: Documentation dependencies (MkDocs, etc.)
- **NLP**: Natural language processing dependencies (spaCy, etc.)

To install only specific groups:

```bash
# Install only documentation dependencies
poetry install --only docs

# Install main dependencies and development dependencies
poetry install --with dev
```

### Building Documentation

```bash
cd uim-docs
poetry run mkdocs build
```

### Running Tests

```bash
poetry run pytest
```

## Get Involved: We Need Your Feedback

We're inviting developers, AI providers, service operators, and tech/AI enthusiasts to review the draft specification, test the implementation, and share feedback. Your input is crucial to refining and improving the protocol.

### How to Contribute

1. **Review the Draft Proposal**: Check out the [draft specification](https://synaptiai.github.io/uim-protocol/specification/uim-specification.txt) and explore the protocol's design and implementation.
2. **Join the Discussion**: Start a conversation in the [Discussions](https://github.com/synaptiai/uim-protocol/discussions) tab. We'd love to hear your thoughts on the protocol's design, potential use cases, or any concerns.
3. **Raise Issues**: Found a bug or have suggestions? Open an [Issue](https://github.com/synaptiai/uim-protocol/issues) to let us know or contribute directly by submitting a Pull Request. See our [Contributing Guidelines](CONTRIBUTING.md) for more information.
4. **Share the Word**: Help us spread the word about the UIM protocol by sharing this repository with your network. Write a blog post, tweet, or share the project with your colleagues. We appreciate your support!

## Protocol Overview

The Unified Intent Mediator (UIM) protocol defines a standardized framework for AI agents to interact with web services through well-defined intents, metadata, and execution methods. By introducing consistency and security in these interactions, UIM enhances efficiency, scalability, and reliability for AI-driven applications.

### Key Components

- **Intents**: Structured actions that web services can expose, defining specific tasks such as searching products, placing orders, or retrieving data.
- **Metadata and Parameters**: Each intent comes with metadata (name, description, category) and defined parameters, providing context and specific input requirements.
- **Policy Adherence Tokens (PATs)**: Digitally signed tokens that encapsulate permissions, billing, and compliance rules.
- **Discovery and Execution APIs**: AI agents can query discovery APIs to find available intents and use execution APIs to perform actions.
- **DNS TXT Records and agents.json Files**: Innovative methods for endpoint discovery, allowing AI agents to find and authenticate API endpoints.

### Architecture Options

The UIM Protocol supports multiple architectural approaches:

1. **Centralized Architecture**: A central repository manages intent registration, discovery, execution, and policy management.
2. **Decentralized Architecture**: AI agents interact directly with web services without a central intermediary.
3. **Hybrid Approach**: Combines centralized discovery with decentralized execution and PAT issuance.

## Repository Structure

```
uim-protocol/
├── implementations/       # Reference implementations
│   ├── centralized-discovery-service/
│   ├── uim-mock-agent/
│   └── uim-mock-webservice/
├── examples/              # Usage examples and demos
├── uim-docs/              # Documentation
│   ├── docs/              # Documentation source files
│   │   ├── specification/ # Protocol specifications
│   │   ├── assets/        # Documentation assets (images, etc.)
│   │   └── reference/     # API reference documentation
│   └── site/              # Generated documentation site
├── pyproject.toml         # Poetry configuration
└── poetry.lock            # Poetry lock file
```

## Current Status & Roadmap

The UIM Protocol is currently in the draft proposal phase. See our roadmap for the development roadmap.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
