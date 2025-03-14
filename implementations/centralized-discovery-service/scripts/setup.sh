#!/bin/bash

# scripts/setup.sh - Script to set up and run the project

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Export database URL (update with your own credentials)
export DATABASE_URL='postgresql://user:password@localhost/uim_db'

# Run database migrations (if any)
# alembic upgrade head  # Uncomment if using Alembic for migrations

# Notify the user
echo "Setup complete. You can now run the application using 'uvicorn app.main:app --reload'."