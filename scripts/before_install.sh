#!/bin/bash

# Update the package index
sudo yum update -y

# Install necessary dependencies (if any)
sudo yum install -y docker

# Start Docker service if not already running
sudo service docker start

# Add user to the Docker group (if not already added)
sudo usermod -aG docker ec2-user

echo "Environment setup completed."
