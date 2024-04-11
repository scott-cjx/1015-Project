# -*- coding: utf-8 -*-
"""1015-WeatherTaxi

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LpTQeT4gPyRUlDsQGtk8NM0j-SkaHR-k
"""

import pandas as pd
import numpy as np
import seaborn as sb
import os

from datetime import datetime
import requests
import logging

logger = logging.getLogger(__name__)
logger.info("Starting weathertaxi.py script")

def get_taxi_avail():
  url = "https://api.data.gov.sg/v1/transport/taxi-availability"

  # Send request and get response
  response = requests.get(url)

  if response.status_code != 200:
    return

  # Parse JSON data
  data = response.json()

  data_coordinates = data['features'][0]['geometry']['coordinates']
  df_coordinates = pd.DataFrame(data_coordinates)
  df_coordinates.columns = ["LONGITUDE", "LATITUDE"]

  ts = data['features'][0]['properties']['timestamp']
  dt_object = datetime.fromisoformat(ts)

  ts_date = dt_object.date()
  ts_time = dt_object.time()
  df_coordinates["DATE"] = ts_date
  df_coordinates["TIME"] = ts_time

  return df_coordinates

taxi_avail = get_taxi_avail()

def get_area_meta():
  url = 'https://api.data.gov.sg/v1/environment/2-hour-weather-forecast'

  # Send request and get response
  response = requests.get(url)

  if response.status_code != 200:
    return

  # Parse JSON data
  data = response.json()
  data_areameta = data['area_metadata']
  df = pd.DataFrame

  return data

def get_weather():
  url = 'https://api.data.gov.sg/v1/environment/2-hour-weather-forecast'

  # Send request and get response
  response = requests.get(url)

  if response.status_code != 200:
    return

  # Parse JSON data
  data = response.json()

  data_weather = data['items'][0]['forecasts']
  df = pd.DataFrame(data_weather)
  df.columns = ["AREA", "FORECAST"]

  ts = data['items'][0]['timestamp']
  df['timestamp'] = ts
  upd_ts = data['items'][0]['update_timestamp']
  df['update_timestamp'] = upd_ts
  valid_start_ts = data['items'][0]['valid_period']['start']
  df['valid_start'] = valid_start_ts
  valid_end_ts = data['items'][0]['valid_period']['end']
  df['valid_end'] = valid_end_ts

  return df


def pandas_to_csv(df, filename):
  #Check if file exists

  #If file exists, append
  #If file does not exist, create
  csv_file_path = os.path.join('/var/pythonbots/sc1015', filename)
  if(os.path.isfile(csv_file_path)):
    df.to_csv(csv_file_path, mode='a', header=False)
  else:
    df.to_csv(csv_file_path)
  


#Get weather data
weather = get_weather()
#Save to csv
pandas_to_csv(weather, 'weather.csv')

#Get taxi availability
taxi_avail = get_taxi_avail()
#Save to csv
pandas_to_csv(taxi_avail, 'taxi.csv')
logger.info("Weathertaxi.py script completed")
