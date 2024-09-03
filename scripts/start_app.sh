#!/bin/bash
echo "Starting the Docker container..."
docker pull 545009869835.dkr.ecr.us-east-1.amazonaws.com/ecr-iris-repo:latest
docker run -d -p 8080:5000 --name ml-iris-app \
  -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
  -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
  -e AWS_DEFAULT_REGION=us-east-1 \
  545009869835.dkr.ecr.us-east-1.amazonaws.com/ecr-iris-repo:latest
