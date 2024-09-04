# Use a public AWS ECR image as the base image
FROM public.ecr.aws/python/python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt .

# Copy the application code into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask (used when running app.py)
EXPOSE 5000

# Default command is to run the Flask app
CMD ["python", "app.py"]
