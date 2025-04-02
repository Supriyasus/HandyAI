# Use Python 3.11 base image
FROM python:3.11

# Install system dependencies for sound and OpenCV
RUN apt-get update && apt-get install -y \
    espeak alsa-utils libgl1 libglib2.0-0 \
    libasound2 libasound2-plugins pulseaudio \
    && rm -rf /var/lib/apt/lists/*

# Set up a dummy sound device for pyttsx3
RUN echo "pcm.!default { type hw card 0 }" > /etc/asound.conf

# Copy application files
COPY . .

# Create and activate a virtual environment
RUN python -m venv venv

# Install dependencies inside the virtual environment
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Expose port (matches your YAML config)
EXPOSE 5000

# Ensure the virtual environment is activated when running the app
CMD ["/app/venv/bin/python", "app.py"]
