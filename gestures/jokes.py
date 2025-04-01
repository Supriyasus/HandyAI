import requests

def fetch_joke():
    """Fetch a random joke from icanhazdadjoke API."""
    url = "https://icanhazdadjoke.com/"
    headers = {
        "Accept": "application/json",
        "User-Agent": "FingerBot (https://fingerbot.com)"  # Update with your app name
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)

        joke_data = response.json()
        return joke_data.get("joke", "Couldn't fetch a joke at the moment. 😂")
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching joke: {e}"

# Example usage:
if __name__ == "__main__":
    print(fetch_joke())
