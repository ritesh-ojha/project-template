#!/bin/bash

# Prompt user for project directory name
read -p "Enter project directory name: " projectName

# Create the main project directory
mkdir "$projectName"

# Copy the issue.py script into the project directory
cp issue.py "$projectName"


cd "$projectName"


# Create directories for different components of the project
mkdir -p src/scripts
mkdir -p src/queries
mkdir -p docs
mkdir -p data/raw
mkdir -p data/processed
mkdir -p config
mkdir -p logs
mkdir -p ISSUE


# Create README.md with basic project information
echo "# $projectName" > README.md
echo "This project is focused on data engineering tasks." >> README.md

# Create directories for documentation and templates
mkdir -p docs/templates

# Create template files
touch src/scripts/etl.py
touch src/queries/example.sql
touch docs/data_dictionary.md
touch config/config.yaml


# Populate template files with basic content
echo "Write your ETL logic here." > src/scripts/etl.py
echo "Write your SQL queries here." > src/queries/example.sql
echo "Describe your data dictionary here." > docs/data_dictionary.md
echo "Define your configurations here." > config/config.yaml

echo "Data Engineering project directory structure created successfully in '$projectName' directory."

# Copy the issue.py script into the project directory
cp issue.py "$projectName"

code .