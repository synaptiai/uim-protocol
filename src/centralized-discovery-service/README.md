# Centralized Intent Discovery Service

This project implements a centralized intent discovery service using FastAPI, enabling AI agents to discover and search for intents across multiple web services as per the UIM protocol.

## Prerequisites

- Python 3.8 or higher
- PostgreSQL database
- pip package manager

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/synaptiai/uim-protocol.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd centralized-intent-discovery
   ```

3. **Configure the database**:

   - Update `app/config.py` with your PostgreSQL database URL.

4. **Run the setup script**:

   ```bash
   bash scripts/setup.sh
   ```

5. **Run the application**:

   ```bash
   uvicorn app.main:app --reload
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

Run the unit tests using:

```bash
python -m unittest discover -s tests
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
