FROM python:3.11

# Install system dependencies
RUN apt-get update && apt-get install -y espeak

# Copy your application files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your app
CMD ["python", "app.py"]  
