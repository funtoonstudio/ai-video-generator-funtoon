#!/bin/bash

echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "Starting AI Video Generator..."
echo ""
echo "Enter your Replicate API token:"
read -p "REPLICATE_API_TOKEN: " REPLICATE_API_TOKEN

export REPLICATE_API_TOKEN=$REPLICATE_API_TOKEN
python app.py
