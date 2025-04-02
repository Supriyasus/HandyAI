FROM python:3.11

# Install system dependencies (including libGL for OpenCV)
RUN apt-get update && apt-get install -y \
    espeak \
    libgl1-mesa-glx  # <-- This fixes the ImportError for OpenCV

# Set up a virtual environment
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Copy application files to root directory
COPY . /

# Install Python dependencies inside the virtual environment
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your app
CMD ["python", "app.py"]
