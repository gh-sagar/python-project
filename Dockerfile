# Use official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy project files
COPY . .

# Command to run your CLI app
CMD ["python", "expense_analyzer/main.py"]
