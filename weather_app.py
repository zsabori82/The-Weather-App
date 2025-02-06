import requests

# Define the API key and base URL for the OpenWeatherMap API
API_KEY = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
'  # Replace with your actual OpenWeatherMap API key
API_URL = 'https://api.openweathermap.org/data/2.5/weather?'

# Function to get weather data based on the city name or latitude/longitude
def get_weather(city=None, lat=None, lon=None, units='metric'):
    """Fetch weather data for the given city or latitude/longitude."""
    
    if city:
        # URL for city name
        url = f'{API_URL}q={city}&appid={API_KEY}&units={units}'
    elif lat and lon:
        # URL for latitude and longitude
        url = f'{API_URL}lat={lat}&lon={lon}&appid={API_KEY}&units={units}'
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

# Main program to interact with the user
def main():
    print("Welcome to the Python Weather App!")
    
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
    
    # Fetch and display the weather
    get_weather(city=city, lat=lat, lon=lon, units=units)

if __name__ == '__main__':
    main()
