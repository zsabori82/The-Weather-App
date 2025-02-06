import requests

# Define the API key and base URL for the OpenWeatherMap API
API_KEY = 'your_actual_api_key_here'  # Replace with your actual OpenWeatherMap API key
API_URL_CURRENT = 'https://api.openweathermap.org/data/2.5/weather?'
API_URL_FORECAST = 'https://api.openweathermap.org/data/2.5/forecast?'

# Function to get current weather data based on the city name or latitude/longitude
def get_current_weather(city=None, lat=None, lon=None, units='metric'):
    """Fetch current weather data for the given city or latitude/longitude."""
    
    if city:
        # URL for city name
        url = f'{API_URL_CURRENT}q={city}&appid={API_KEY}&units={units}'
    elif lat and lon:
        # URL for latitude and longitude
        url = f'{API_URL_CURRENT}lat={lat}&lon={lon}&appid={API_KEY}&units={units}'
    else:
        print("Please provide either a city name or latitude and longitude.")
        return
    
    # Make the HTTP request to the OpenWeatherMap API
    response = requests.get(url)
    
    # If the request is successful
    if response.status_code == 200:
        data = response.json()
        # Extract relevant weather details
        city_name = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        condition = data['weather'][0]['description']
        
        # Print weather details to the user
        print(f"Weather in {city_name}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Condition: {condition}")
    
    else:
        print("City not found. Please try again.")

# Function to get weather forecast data based on the city name or latitude/longitude
def get_weather_forecast(city=None, lat=None, lon=None, units='metric'):
    """Fetch weather forecast data for the given city or latitude/longitude."""
    
    if city:
        # URL for city name
        url = f'{API_URL_FORECAST}q={city}&appid={API_KEY}&units={units}'
    elif lat and lon:
        # URL for latitude and longitude
        url = f'{API_URL_FORECAST}lat={lat}&lon={lon}&appid={API_KEY}&units={units}'
    else:
        print("Please provide either a city name or latitude and longitude.")
        return
    
    # Make the HTTP request to the OpenWeatherMap API
    response = requests.get(url)
    
    # If the request is successful
    if response.status_code == 200:
        data = response.json()
        # Extract and print the forecast details for the next 5 days
        print(f"Weather Forecast:")
        for item in data['list']:
            # Extract forecast details from each item (3-hour intervals)
            timestamp = item['dt_txt']
            temperature = item['main']['temp']
            condition = item['weather'][0]['description']
            print(f"{timestamp}: Temperature: {temperature}°C, Condition: {condition}")
    
    else:
        print("Forecast not found. Please try again.")

# Main program to interact with the user
def main():
    print("Welcome to the Python Weather App!")
    
    # Ask the user for the choice between current weather or forecast
    weather_choice = input("Enter '1' for current weather or '2' for weather forecast: ").strip()
    
    # Ask the user for the choice between city or coordinates
    location_choice = input("Enter '1' to search by city name or '2' to search by latitude/longitude: ").strip()

    # Handle city name input
    if location_choice == '1':
        city = input("Enter the name of the city: ")
        lat = lon = None
    
    # Handle latitude and longitude input
    elif location_choice == '2':
        city = None
        lat = float(input("Enter the latitude: "))
        lon = float(input("Enter the longitude: "))
    else:
        print("Invalid choice, please enter '1' or '2'.")
        return
    
    # Optionally, prompt for unit selection
    unit_choice = input("Enter 'C' for Celsius or 'F' for Fahrenheit: ").strip().upper()
    if unit_choice == 'F':
        units = 'imperial'
    else:
        units = 'metric'

    # Fetch and display the weather or forecast
    if weather_choice == '1':
        get_current_weather(city=city, lat=lat, lon=lon, units=units)
    elif weather_choice == '2':
        get_weather_forecast(city=city, lat=lat, lon=lon, units=units)
    else:
        print("Invalid choice, please enter '1' or '2'.")
        return

if __name__ == '__main__':
    main()
