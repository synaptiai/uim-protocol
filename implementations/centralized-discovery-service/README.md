# Centralized Intent Discovery Service

This project implements a centralized intent discovery service using FastAPI, enabling AI agents to discover and search for intents across multiple web services as per the UIM protocol.

## Prerequisites

- Python 3.10 or higher
- PostgreSQL database
- [Poetry](https://python-poetry.org/) for dependency management

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/synaptiai/uim-protocol.git
   cd uim-protocol
   ```

2. **Install dependencies with Poetry**:

   ```bash
   # Install Poetry if you haven't already
   curl -sSL https://install.python-poetry.org | python3 -

   # Install dependencies
   poetry install
   ```

3. **Navigate to the implementation directory**:

   ```bash
   cd implementations/centralized-discovery-service
   ```

4. **Configure the database**:

   - Create a `.env` file based on `.env.example` with your PostgreSQL database URL.

5. **Run the application with Poetry**:

   ```bash
   # Activate the virtual environment
   poetry shell

   # Run the application
   uvicorn app.main:app --reload
   ```

   Alternatively, you can use Docker:

   ```bash
   docker-compose up
   ```

## API Endpoints

- **Discovery**:
  - `GET /api/intents/search`: Search for intents based on criteria.
  - `GET /api/search/`: Search intents using a natural language query.

## Crawling Mechanism

- The crawler starts on application startup.
- It fetches `agents.json` files using DNS TXT records or directly.
- Intents are stored in the PostgreSQL database for fast querying.

## Testing

Run the unit tests using Poetry:

```bash
# From the root directory
poetry run pytest implementations/centralized-discovery-service/tests

# Or if you're in the virtual environment
pytest tests
```

## Configuration

Modify `app/config.py` to change application settings such as the database URL.

## License

This project is licensed under the Apache License 2.0.

## Contributing suggestions

1. Implement authentication and rate limiting for API endpoints.
2. Extend natural language processing capabilities for better query handling.
3. Add a web interface for monitoring crawled intents.
4. Integrate a scheduler to periodically update the intent index.
5. Deploy the application using a production-grade server like Gunicorn.
6. Add CI/CD Pipeline: Use GitHub Actions to automate testing and deployment.
7. Include Code Quality Tools: Integrate tools like flake8, black, and isort for code formatting and linting.
8. Enhance NLP Capabilities: Use a library like spaCy or NLTK for advanced natural language processing in the search functionality.
9. Add a Frontend Interface: Optionally, create a simple web interface using React or Vue.js for users to interact with the service.
