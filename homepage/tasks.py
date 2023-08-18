import requests
import os
from django.core.cache import cache
from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler()
lat = os.environ['LAT']
lon = os.environ['LON']
appid = os.environ['APP_ID']

def weather_updater():
    raw_wather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}")
    current_weather = raw_wather.text
    cache.set("weather", current_weather)

scheduler.add_job(weather_updater, 'interval', seconds=30)
scheduler.start()





