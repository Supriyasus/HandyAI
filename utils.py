import cv2
from cvzone.HandTrackingModule import HandDetector
from gestures.weather import fetch_weather
from gestures.jokes import fetch_joke
import pyttsx3
import threading

def speak_text(text):
    """Speaks the given text in a separate thread to avoid runtime errors."""
    def _speak():
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    thread = threading.Thread(target=_speak)
    thread.start()

def perform_action(image_path):
    """Detect fingers in an image and perform predefined actions."""

    # Read the uploaded image
    photo = cv2.imread(image_path)
    if photo is None:
        return {"message": "Error loading the image."}

    # Initialize hand detector
    detector = HandDetector(detectionCon=0.5, maxHands=1)

    # Detect hands in the image
    hands, _ = detector.findHands(photo, draw=False)  # Unpack tuple

    if hands:
        hand_info = hands[0]  # Extract first hand
        fingers = detector.fingersUp(hand_info)  # Get raised fingers
        count = sum(fingers)  # Count raised fingers

        # Default location for weather API
        default_lat, default_lon = 28.6139, 77.2090

        # Define web-based actions for specific gestures
        actions = {
            5: lambda: {"message": "Opening Times of India", "url": "https://timesofindia.indiatimes.com/us"},
            4: lambda: {"message": fetch_joke()},
            3: lambda: {"message": "Opening YouTube", "url": "https://youtube.com"},
            2: lambda: {"message": fetch_weather(default_lat, default_lon)},
            1: lambda: {"message": "Opening ChatGPT", "url": "https://chat.openai.com"}
        }

        return actions.get(count, lambda: {"message": "Gesture not recognized"})()

    return {"message": "No hands detected."}
