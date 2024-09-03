#!/bin/bash

	# Stop any existing containers
	docker stop $(docker ps -a -q) || true
	docker rm $(docker ps -a -q) || true

	# Pull the latest Docker image from ECR
	docker pull ecr-iris-repo:latest

	# Run the Docker container
	docker run -d -p 5000:5000 ecr-iris-repo:latest
