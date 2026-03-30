# 1. Use a standard Python image (avoiding slim for better compatibility with CV libraries)
FROM python:3.9

# 2. Update and install system dependencies in a single layer to prevent caching errors
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 3. Set the working directory
WORKDIR /app

# 4. Upgrade pip first
RUN pip install --upgrade pip

# 5. Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of your application
COPY . .

# 7. Use Gunicorn for production (Render strictly prefers this over Flask's debug server)
# The timeout is set to 120 to allow the AI model time to process images
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000", "--timeout", "120"]
