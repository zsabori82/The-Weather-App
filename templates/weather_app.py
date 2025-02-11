from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "aa48cf6e738308576fcb52d78d515e73"  # Your OpenWeatherMap API key
API_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city, units="metric"):
    """Fetch current weather data for the given city."""
    url = f"{API_URL}?q={city}&appid={API_KEY}&units={units}"
    
    # Debugging: print the API URL
    print(f"Fetching weather from: {url}")
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Debugging: print the data received from the API
        print(f"API Response: {data}")
        
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"]
        }
    else:
        # Debugging: print error if API request fails
        print(f"API Error: {response.status_code} - {response.text}")
        return None  # Return None if city is not found

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error_message = None
    
    if request.method == "POST":
        city = request.form["city"]
        units = request.form["units"]

        weather = get_weather(city, units)
        
        if weather is None:
            error_message = f"City '{city}' not found. Please try again."
    
    return render_template("index.html", weather=weather, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
