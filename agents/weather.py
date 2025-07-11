# Import requests to call the weather API
import requests

# Function to get a 3-day weather forecast for a destination
def get_weather_forecast(destination: str) -> str:
    # Define latitude and longitude for supported destinations
    location_map = {
        "Bali": (-8.4095, 115.1889),
        "Cairns": (-16.9186, 145.7781),
        "Gold Coast": (-28.0167, 153.4000),
        "Bangkok": (13.7563, 100.5018),
    }

    # If destination not in list, return an error message
    if destination not in location_map:
        return "Weather data unavailable."

    # Get latitude and longitude
    lat, lon = location_map[destination]

    # Construct API URL for 3-day forecast (max temp and rain)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,precipitation_sum&timezone=auto"

    # Make the request
    response = requests.get(url)

    # Handle failed requests
    if response.status_code != 200:
        return "Failed to fetch weather data."

    # Parse weather forecast data
    data = response.json()
    forecast = data["daily"]
    temp = forecast["temperature_2m_max"][:3]     # First 3 days of max temps
    rain = forecast["precipitation_sum"][:3]      # First 3 days of rain

    # Format the forecast summary for 3 days
    summary = "\n".join([
        f"Day {i+1}: Max Temp {temp[i]}°C, Rain: {rain[i]}mm"
        for i in range(3)
    ])

    # Return the weather forecast in a readable format
    return f"🌤️ Weather forecast for {destination}:\n{summary}"
