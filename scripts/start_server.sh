#!/bin/bash

	# Stop any existing containers
	sudo docker stop $(docker ps -a -q) || true
	sudo docker rm $(docker ps -a -q) || true

	# Pull the latest Docker image from ECR
	sudo docker pull ecr-iris-repo:latest

	# Run the Docker container
	sudo docker run -d -p 8080:5000 ecr-iris-repo:latest
