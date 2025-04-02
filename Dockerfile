# Use Python 3.11 base image
FROM python:3.11

# Install system dependencies
RUN apt-get update && apt-get install -y \
    espeak alsa-utils libgl1 libglib2.0-0 \
    libasound2 libasound2-plugins pulseaudio

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Create and activate a virtual environment
RUN python -m venv venv

# Install dependencies inside the virtual environment
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Set up a dummy sound device
RUN echo "pcm.!default { type plug slave.pcm 'null' }" > /etc/asound.conf

# Ensure the virtual environment is activated when running the app
CMD ["/app/venv/bin/python", "app.py"]
