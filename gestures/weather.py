import requests
import os
from dotenv import load_dotenv

load_dotenv()  

WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")

def fetch_weather(lat, lon):
    """Fetch weather using latitude & longitude."""
    if not WEATHERSTACK_API_KEY:
        return "⚠️ API key missing."

    base_url = "http://api.weatherstack.com/current"
    params = {
        "access_key": WEATHERSTACK_API_KEY,
        "query": f"{lat},{lon}",
        "units": "m"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if "current" in data:
            temp = data["current"]["temperature"]
            condition = data["current"]["weather_descriptions"][0]
            return f"🌤️ {temp}°C, {condition}"
        else:
            return "⚠️ Unable to fetch weather data."
    except Exception as e:
        return f"⚠️ Error fetching weather: {str(e)}"
