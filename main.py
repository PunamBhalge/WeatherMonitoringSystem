from apscheduler.schedulers.blocking import BlockingScheduler
from data_processor import store_weather_data, calculate_daily_summary
from weather_api import get_weather_data
from alert import check_alerts
from config import CITIES, INTERVAL

def monitor_weather():
    weather_data = [get_weather_data(city) for city in CITIES]
    store_weather_data(weather_data)
    calculate_daily_summary()
    check_alerts()

if __name__ == "__main__":
    print("$#########")
    scheduler = BlockingScheduler()
    scheduler.add_job(monitor_weather, 'interval', minutes=INTERVAL)
    scheduler.start()
