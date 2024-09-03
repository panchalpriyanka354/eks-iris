#!/bin/bash
echo "Stopping and removing the Docker container..."
docker stop ml-iris-app || true
docker rm ml-iris-app || true
