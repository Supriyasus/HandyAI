# HandyAI - Hand Gesture Recognition and Automation

HandyAI is a web-based application that uses hand gesture recognition to trigger various actions. The system leverages computer vision and machine learning to detect hand gestures and perform predefined tasks. It also uses text-to-speech functionality to announce the actions it performs, making it an interactive and user-friendly application.


##  Features

- **Hand Gesture Recognition**: Detects various hand gestures using a webcam.
- **Speech Output**: Announces the action being performed (e.g., "Opening YouTube").
- **Automated Actions**: Based on hand gestures, the application can:
  - Open websites
  - Fetch weather updates
  - Retrieve jokes
  - Display news articles
  - Perform other predefined tasks
- **Interactive Web Interface**: Built using HTML, CSS, and JavaScript, with real-time webcam feed.

---

## Requirements

To run this project, you need the following dependencies:

- Python 3.x
- Flask
- OpenCV
- pyttsx3
- cvzone
- requests
- dotenv (for managing environment variables)
- News API (for fetching news articles)

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Supriyasus/HandyAI.git
cd HandyAI
```
### 2. Install Dependencies
Step 1: Create a Virtual Environment
```bash
python -m venv venv
```
Step 2: Activate the Virtual Environment
```bash
venv\Scripts\activate #windows
source venv/bin/activate #macOS/Linux
```
Step 3: Install Required Python Packages
```bash
pip install -r requirements.txt
```

## Set Up API Keys
- Sign up for the WeatherStack API (https://weatherstack.com/) and get   your API key.
- Sign up for the NewsAPI (https://newsapi.org/) to get your News API key.
- Add in .env file:
```bash
WEATHERSTACK_API_KEY=your_weatherstack_api_key
NEWSAPI_KEY=your_newsapi_key
```
## Run the Application
```bash
python app.py
```
This will start the Flask server on http://localhost:5000/.
