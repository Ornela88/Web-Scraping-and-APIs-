import requests
import pandas as pd
from datetime import datetime

def fetch_weather_data(API_key, city):
    try:
        # Construct the API URL
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}&units=metric"
        response = requests.get(url)

        # Check for successful response
        if response.status_code == 200:
            weather_json = response.json()

            # Validate the expected structure in the response
            if "list" in weather_json:
                temperature = weather_json["list"][0]["main"]["temp"]
                description = weather_json["list"][0]['weather'][0]['description']
                feels_like = weather_json["list"][0]["main"].get("feels_like")
                wind_speed = weather_json["list"][0]["wind"].get("speed")

                # Create a DataFrame with the weather data
                return pd.DataFrame({
                    "forecast_time": [datetime.now()],
                    "outlook": [description],
                    "temperature": [temperature],
                    "feels_like": [feels_like],
                    "wind_speed": [wind_speed]
                })
            else:
                print("Unexpected response format: 'list' key not found.")
        else:
            print(f"Failed to fetch data for {city}. Status Code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred while fetching data: {str(e)}")

    # Return an empty DataFrame in case of any failure
    return pd.DataFrame()


