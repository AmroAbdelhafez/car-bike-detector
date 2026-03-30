# 1. Use the standard Python base image
FROM python:3.9

# 2. Set the working directory
WORKDIR /app

# 3. Install the missing system library for OpenCV
RUN apt-get update && apt-get install -y libgl1

# 4. Upgrade pip and install Python packages
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your application code
COPY . .

# 6. Run the app using Gunicorn (Letting Render handle the port)
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
