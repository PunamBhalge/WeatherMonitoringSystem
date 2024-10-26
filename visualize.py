import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql://user:pass@localhost:5432/weather_db")

def plot_daily_summary():
    df = pd.read_sql("SELECT * FROM daily_summary", engine)
    df['day'] = pd.to_datetime(df['day'])
    
    plt.plot(df['day'], df['avg_temp'], label='Average Temperature')
    plt.plot(df['day'], df['max_temp'], label='Max Temperature')
    plt.plot(df['day'], df['min_temp'], label='Min Temperature')
    
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Daily Weather Summary')
    plt.legend()
    plt.show()
