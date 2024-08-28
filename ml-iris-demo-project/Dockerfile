# Base image
FROM python:3.8-slim

# Set the working directory
#WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt .

COPY . .

# Install dependencies
RUN pip install -r requirements.txt


# Set environment variables for AWS access
ENV AWS_ACCESS_KEY_ID=AKIA2UC3CX7ON4KNN4YV
ENV AWS_SECRET_ACCESS_KEY=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
ENV AWS_DEFAULT_REGION=us-east-2

# Run the training script
CMD ["python", "model.py"] 



