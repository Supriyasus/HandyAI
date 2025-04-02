import cv2
from cvzone.HandTrackingModule import HandDetector
from gestures.weather import fetch_weather
from gestures.jokes import fetch_joke
import threading
import pyttsx3

def speak_action(message):
    """Function to handle speech in a separate thread."""
    engine = pyttsx3.init(driverName="espeak")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Female voice
    engine.setProperty('rate', 150)  # Adjust speech rate
    engine.say(message)
    engine.runAndWait()

def perform_action(image_path):
    """Detect fingers in an image and perform predefined actions."""
    photo = cv2.imread(image_path)
    if photo is None:
        return {"message": "Error loading the image."}

    detector = HandDetector(detectionCon=0.5, maxHands=1)
    hands, _ = detector.findHands(photo, draw=False)

    if hands:
        hand_info = hands[0]
        fingers = detector.fingersUp(hand_info)
        count = sum(fingers)

        actions = {
            5: lambda: {"message": "Opening Times of India", "url": "https://timesofindia.indiatimes.com/us"},
            4: lambda: {"message": fetch_joke()},
            3: lambda: {"message": "Opening YouTube", "url": "https://youtube.com"},
            2: lambda: {"message": fetch_weather(28.6139, 77.2090)},
            1: lambda: {"message": "Opening ChatGPT", "url": "https://chat.openai.com"}
        }

        action = actions.get(count, lambda: {"message": "Gesture not recognized"})()

        # Speak the action in a separate thread
        threading.Thread(target=speak_action, args=(action['message'],)).start()

        return action

    return {"message": "No hands detected."}
