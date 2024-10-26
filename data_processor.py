import pandas as pd
from sqlalchemy import create_engine
from config import CITIES
from weather_api import get_weather_data

engine = create_engine("postgresql://user:pass@localhost:5432/weather_db")

def store_weather_data(data):
    df = pd.DataFrame(data)
    df.to_sql("weather_data", con=engine, if_exists="append", index=False)

def calculate_daily_summary():
    query = """SELECT date_trunc('day', to_timestamp(dt)) AS day,
                      avg(temp) AS avg_temp,
                      max(temp) AS max_temp,
                      min(temp) AS min_temp,
                      mode() WITHIN GROUP (ORDER BY main) AS dominant_weather
               FROM weather_data
               GROUP BY day"""
    summary = pd.read_sql(query, engine)
    summary.to_sql("daily_summary", con=engine, if_exists="replace", index=False)
