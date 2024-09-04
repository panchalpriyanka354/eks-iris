#!/bin/bash

# Wait for a few seconds to allow the app to start
sleep 10

# Validate that the application is running
curl -f http://localhost:8080 || {
  echo "Validation failed. The application is not running correctly."
  exit 1
}

echo "Validation succeeded. The application is running correctly."
