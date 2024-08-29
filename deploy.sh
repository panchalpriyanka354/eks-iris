#!/bin/bash

# Fail on any error
set -e

# Define variables
NAMESPACE="default"  # Kubernetes namespace (adjust if needed)
DEPLOYMENT_FILE="deployment.yaml"
SERVICE_FILE="service.yaml"
LOG_FILE="/tmp/deploy.log"

# Start logging
echo "Deployment started at $(date)" | tee -a $LOG_FILE

# Apply Kubernetes deployment configuration
echo "Applying Kubernetes deployment configuration from $DEPLOYMENT_FILE..." | tee -a $LOG_FILE
kubectl apply -f $DEPLOYMENT_FILE --namespace=$NAMESPACE | tee -a $LOG_FILE

# Apply Kubernetes service configuration
echo "Applying Kubernetes service configuration from $SERVICE_FILE..." | tee -a $LOG_FILE
kubectl apply -f $SERVICE_FILE --namespace=$NAMESPACE | tee -a $LOG_FILE

# Check deployment status
echo "Checking deployment status..." | tee -a $LOG_FILE
kubectl rollout status deployment/$(grep 'name:' $DEPLOYMENT_FILE | awk '{print $2}') --namespace=$NAMESPACE | tee -a $LOG_FILE

# Log end time
echo "Deployment completed at $(date)" | tee -a $LOG_FILE

# Print logs for debugging
cat $LOG_FILE
