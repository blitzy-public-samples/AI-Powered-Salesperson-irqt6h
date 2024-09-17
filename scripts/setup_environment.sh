#!/bin/bash

# Check for required tools
check_tool() {
    if ! command -v $1 &> /dev/null
    then
        echo "$1 is not installed. Please install it and try again."
        exit 1
    fi
}

check_tool docker
check_tool python3
check_tool node

# Install project dependencies
echo "Installing project dependencies..."
pip3 install -r requirements.txt
npm install

# Set up virtual environments
echo "Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Configure environment variables
echo "Configuring environment variables..."
cp .env.example .env
# HUMAN ASSISTANCE NEEDED
# TODO: Update .env file with appropriate values

# Initialize local database
echo "Initializing local database..."
docker-compose up -d db
# HUMAN ASSISTANCE NEEDED
# TODO: Add commands to run database migrations or initial setup

# Set up pre-commit hooks
echo "Setting up pre-commit hooks..."
pre-commit install

echo "Environment setup complete!"