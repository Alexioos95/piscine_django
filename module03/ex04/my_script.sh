#!/bin/bash

echo "Creating venv 'django_venv'..."
python3 -m venv django_venv

echo "Activating venv..."
source ./django_venv/bin/activate

echo "Installing requirements from 'requirement.txt'..."
pip install -r "requirement.txt"
