from config import THRESHOLD
from sqlalchemy import create_engine

engine = create_engine("postgresql://user:pass@localhost:5432/weather_db")

def check_alerts():
    query = "SELECT temp FROM weather_data ORDER BY dt DESC LIMIT 2"
    result = engine.execute(query).fetchall()
    if len(result) == 2 and result[0][0] > THRESHOLD and result[1][0] > THRESHOLD:
        print("Alert: Temperature exceeded 35°C for two consecutive updates.")
