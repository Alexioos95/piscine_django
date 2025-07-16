#!/bin/bash

echo "Creating venv 'venv'..."
python3 -m venv venv

echo "Activating venv..."
source ./venv/bin/activate

echo "Installing requirements from 'requirement.txt'..."
pip install -r "requirement.txt"

echo "Starting server..."
python3 hello_world/manage.py runserver
