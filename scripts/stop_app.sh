#!/bin/bash
echo "Stopping and removing the Docker container..."
sudo docker stop ml-iris-app || true
sudo docker rm ml-iris-app || true
