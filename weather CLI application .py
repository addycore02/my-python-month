import requests

print("    WEATHER CLI APPLICATION    ")

city = input("Enter City Name : ").strip()

try:
    # GET CITY COORDINATES
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    geo_response = requests.get(geo_url, params=geo_params)
    geo_data = geo_response.json()

    # Safely check if results exist and contain at least 1 match
    results = geo_data.get("results")

    if not results:
        print("City not found.")
    else:
        first_result = results[0]
        latitude = first_result["latitude"]
        longitude = first_result["longitude"]
        city_name = first_result["name"]
        country = first_result.get("country", "N/A")

        # WEATHER API URL
        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
            "timezone": "auto"
        }

        weather_response = requests.get(weather_url, params=weather_params)
        weather_data = weather_response.json()

        current_weather = weather_data["current"]

        temperature = current_weather["temperature_2m"]
        humidity = current_weather["relative_humidity_2m"]
        wind_speed = current_weather["wind_speed_10m"]
        weather_code = current_weather["weather_code"]

        # DISPLAY WEATHER
        print("\n========== WEATHER ==========")
        print("City        :", city_name)
        print("Country     :", country)
        print("Temperature :", temperature, "°C")
        print("Humidity    :", humidity, "%")
        print("Wind Speed  :", wind_speed, "km/h")
        print("Weather Code:", weather_code)

except requests.exceptions.RequestException:
    print("Unable to connect to the weather service.")

except Exception as error:
    print("Something went wrong:", error)