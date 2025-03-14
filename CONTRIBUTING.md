# Contributing to the UIM Protocol

Thank you for your interest in contributing to the Unified Intent Mediator (UIM) Protocol! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before contributing.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the [issue list](https://github.com/synaptiai/uim-protocol/issues) to avoid duplicates. When you create a bug report, include as many details as possible:

1. Use a clear and descriptive title
2. Describe the exact steps to reproduce the problem
3. Describe the behavior you observed and what you expected to see
4. Include screenshots if possible
5. Specify your environment (OS, browser, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

1. Use a clear and descriptive title
2. Provide a detailed description of the suggested enhancement
3. Explain why this enhancement would be useful
4. Specify which area of the protocol it affects (e.g., discovery, execution, policy)

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes
4. Ensure your code follows the project's style guidelines
5. Write or update tests as needed
6. Update documentation as needed
7. Submit a pull request

## Development Process

### Setting Up the Development Environment

1. Clone the repository
   ```bash
   git clone https://github.com/synaptiai/uim-protocol.git
   cd uim-protocol
   ```

2. Install Poetry (if not already installed)
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install dependencies with Poetry
   ```bash
   poetry install
   ```

4. Activate the virtual environment
   ```bash
   poetry shell
   ```

5. Set up pre-commit hooks
   ```bash
   poetry run pre-commit install
   ```

### Working with Poetry

This project uses Poetry for dependency management. Here are some common commands:

- **Add a new dependency**:
  ```bash
  poetry add package-name
  ```

- **Add a development dependency**:
  ```bash
  poetry add --group dev package-name
  ```

- **Update dependencies**:
  ```bash
  poetry update
  ```

- **Run a command in the virtual environment**:
  ```bash
  poetry run command
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

### Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality. The hooks run automatically when you commit changes, but you can also run them manually:

```bash
poetry run pre-commit run --all-files
```

The following hooks are configured:

- **Code Formatting**: Black and isort for consistent code style
- **Linting**: Flake8, Pylint, and MyPy for code quality
- **File Checks**: Trailing whitespace, end-of-file fixing, YAML/TOML validation
- **Markdown Linting**: Ensures consistent Markdown formatting

### Coding Standards

- Follow PEP 8 style guide for Python code
- Use [Black](https://black.readthedocs.io/) for code formatting
- Use [isort](https://pycqa.github.io/isort/) for import sorting
- Use meaningful variable and function names
- Write clear comments and documentation
- Keep functions small and focused on a single task

### Testing

- Write tests for new features and bug fixes
- Run tests with Poetry:
  ```bash
  poetry run pytest
  ```
- Ensure all tests pass before submitting a pull request
- Aim for high test coverage

### Documentation

- Update documentation for any changes to the protocol
- Use clear and concise language
- Include examples where appropriate
- Build documentation with Poetry:
  ```bash
  cd uim-docs
  poetry run mkdocs build
  ```

## Contact Information

If you have questions or need help, you can:

- Open an issue on GitHub
- Join our [Discord server](https://discord.gg/your-discord-invite)
- Email the maintainers at [uim-protocol@synapti.ai](mailto:uim-protocol@synapti.ai)

## Recognition

Contributors will be acknowledged in the project's documentation and release notes.

Thank you for contributing to the UIM Protocol!
