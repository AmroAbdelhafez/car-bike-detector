# Use the standard Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Install the missing system library for OpenCV
RUN apt-get update && apt-get install -y libgl1

# Upgrade pip and install Python packages
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY . .

# Expose port 5001 to match Flask
EXPOSE 5001

# Run the app
CMD ["python", "app.py"]