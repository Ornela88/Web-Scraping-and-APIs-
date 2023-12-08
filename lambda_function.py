import json
import pandas as pd
import os
import sqlalchemy
from weather_function import fetch_weather_data  # make sure this is the updated function without 'city'

def lambda_handler(event, context):
    # Database configuration
    schema = "gans"
    host = "wbs-ornela-project3-db.ctonxk9cu99m.us-west-1.rds.amazonaws.com"  # Replace with your RDS endpoint
    user = "admin"
    password = os.environ["DB_PASSWORD"]  # Environment variable for the password
    port = 3306
    con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'

    # List of cities
    cities = ["Berlin", "Frankfurt"]
    weather_df = pd.DataFrame()

    # Fetch weather data for each city and append to the DataFrame
    for city in cities:
        city_weather_df = fetch_weather_data(os.environ['WEATHER_API_KEY'], city)
        if not city_weather_df.empty:
            weather_df = pd.concat([weather_df, city_weather_df], ignore_index=True)

    # Write the weather data to the SQL database
    weather_df.to_sql('weather', con=con, if_exists='append', index=False)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

