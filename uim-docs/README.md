# UIM Protocol Documentation

This directory contains the documentation for the Universal Intent Markup (UIM) Protocol. The documentation is built using [MkDocs](https://www.mkdocs.org/) with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

1. Install MkDocs and the Material theme:

```bash
pip install mkdocs mkdocs-material
```

2. Install additional dependencies:

```bash
pip install mkdocs-minify-plugin
```

### Building the Documentation

To build the documentation site:

```bash
./build-docs.sh
```

This will create a `site` directory containing the built documentation.

### Serving the Documentation Locally

To serve the documentation locally:

```bash
mkdocs serve
```

This will start a local server at http://localhost:8000.

### Deploying the Documentation

To deploy the documentation to GitHub Pages:

```bash
mkdocs gh-deploy
```

## Documentation Structure

The documentation is organized into the following sections:

- **Specification**: Detailed specification of the UIM Protocol
- **Guides**: Implementation guides for AI agents and web services
- **Reference**: Technical reference for the UIM Protocol
- **Prototypes**: Information about the prototype implementations
- **Community**: Information about the UIM Protocol community

## Contributing

Contributions to the documentation are welcome! Please see the [Contributing Guide](docs/community/contributing.md) for more information.

## License

The UIM Protocol documentation is licensed under the Apache 2.0 License. See the [LICENSE](../LICENSE) file for details.
