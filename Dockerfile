FROM python:3.11

RUN apt-get update && apt-get install -y \
    espeak alsa-utils libgl1 libglib2.0-0 \
    libasound2 libasound2-plugins pulseaudio \
    && rm -rf /var/lib/apt/lists/*

RUN echo "pcm.!default { type hw card 0 }" > /etc/asound.conf

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
