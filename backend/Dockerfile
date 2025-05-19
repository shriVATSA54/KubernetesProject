FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy only necessary files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose the Flask app port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
