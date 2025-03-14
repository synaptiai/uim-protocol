# Technical Specification

## System Overview
The system consists of a mock web service (`uim-mock-webservice`) and a centralized discovery service (`centralized-discovery-service`), designed to facilitate secure communication and service discovery within a microservices architecture. The `uim-mock-webservice` uses RSA key pairs for secure data transmission, while the `centralized-discovery-service` provides a mechanism for services to register and discover each other, leveraging Docker for containerization and Postgres for persistent storage.

### Main Components
- **uim-mock-webservice:** Simulates a web service using secure communication via RSA keys.
- **centralized-discovery-service:** A service registry and discovery mechanism using Docker and Postgres.
- **Database:** Postgres database for persistent storage of service registrations.

## Core Functionality

### Secure Communication via RSA Keys
- **Importance Score: 80**
- **Description:** 
  - The system utilizes RSA key pairs located in `uim-mock-webservice/keys` and `uim-mock-agent/keys/http_localhost_4000` for encrypting and decrypting data. These keys ensure that communication between services is secure and integrity is maintained.

### Dockerfile Configuration
- **Importance Score: 90**
- **Description:**
  - The `Dockerfile` located in `centralized-discovery-service` configures the build process for the service container.
  - **Base Image:** `python:3.8-slim`
  - **Working Directory:** `/app`
  - **Dependencies:** Installs Python dependencies specified in `requirements.txt`.
  - **Command:** Executes the application using `uvicorn` with the app instance at `app.main:app`, binding to `0.0.0.0:8000`.

### Docker Compose Configuration
- **Importance Score: 90**
- **Description:**
  - The `docker-compose.yml` file orchestrates the deployment of the `centralized-discovery-service`.
  - **Services:**
    - **Web Service:**
      - Builds the image from the current directory.
      - Exposes port `8000`.
      - Depends on the `db` service.
      - Utilizes the `DATABASE_URL` environment variable for database connectivity.
    - **Database Service:**
      - Employs the `postgres:13` image.
      - Configures Postgres with environment variables.
      - Establishes volumes for durable database storage.

### Pytest Configuration
- **Importance Score: 70**
- **Description:**
  - The `pytest.ini` file configures pytest to utilize an asyncio event loop scoped to the function level, crucial for asynchronous test functions within the service.

### Setup Script
- **Importance Score: 85**
- **Description:**
  - The `setup.sh` script located in `centralized-discovery-service/scripts` automates the setup process.
  - **Virtual Environment:** Creates and activates a Python virtual environment.
  - **Dependency Installation:** Installs project dependencies from `requirements.txt`.
  - **Database URL:** Configures the `DATABASE_URL` environment variable for database connection.
  - **Notification:** Alerts the user upon completion of setup and provides a command to launch the application.

## Architecture
The system architecture revolves around secure communication and service discovery. Data flows into the `centralized-discovery-service` via API requests, where it is processed and stored in the Postgres database. Services register themselves with the discovery service, which then facilitates their discovery by other services within the ecosystem. Secure communication is ensured through the use of RSA key pairs, which encrypt and decrypt data as it traverses between services.