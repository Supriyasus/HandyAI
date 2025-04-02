FROM python:3.11

# Install system dependencies
RUN apt-get update && apt-get install -y \
    espeak alsa-utils libgl1 libglib2.0-0

# Set working directory (adjust if needed)
WORKDIR /

# Copy your application files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your app
CMD ["python", "app.py"]
