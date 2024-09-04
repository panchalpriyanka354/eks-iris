#!/bin/bash

# Stop the Docker container if it's running
sudo docker stop ml-iris-app || true

# Remove the stopped container
sudo docker rm ml-iris-app || true

echo "Docker container ml-iris-app stopped and removed successfully."
