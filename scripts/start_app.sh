#!/bin/bash

# Step 1: Export AWS Credentials (use this cautiously; IAM roles are preferred)
export AWS_ACCESS_KEY_ID=AKIAX5ZI6UQFQA44MQWM
export AWS_SECRET_ACCESS_KEY=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
export AWS_DEFAULT_REGION=us-east-1

# Step 2: Log in to Amazon ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 545009869835.dkr.ecr.us-east-1.amazonaws.com

# Step 3: Pull the latest Docker image from ECR
sudo docker pull 545009869835.dkr.ecr.us-east-1.amazonaws.com/ecr-iris-repo:latest

# Step 4: Stop and remove any existing container with the same name
sudo docker stop ml-iris-app || true
sudo docker rm ml-iris-app || true

# Step 5: Run the Docker container with the latest image
sudo docker run -d -p 8080:5000 --name ml-iris-app \
  -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
  -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
  -e AWS_DEFAULT_REGION=us-east-1 \
  545009869835.dkr.ecr.us-east-1.amazonaws.com/ecr-iris-repo:latest

echo "Docker container ml-iris-app deployed successfully on Dev/QA environment."
