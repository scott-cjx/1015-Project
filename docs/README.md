# Predicting Taxi Availability Depending on Weather Conditions

This is a mini-project for SC 1015 (Introduction to Data Science and Artificial Intelligence). Our team's objective is to predict the availability of taxis in Singapore based on weather conditions. 

1. [Data Collection](#data-collection)
2. [Data Cleaning and Preparation](#data-cleaning-and-preparation)
3. [Exploratory Data Analysis](#exploratory-data-analysis)
4. [Model Building](#model-building)
5. [Model Evaluation](#model-evaluation)
6. [Conclusion](#conclusion)

## Data Collection

The data was collected from the following sources:
1. Taxi Availability Data
: This API contains the availability of taxis in Singapore from 2016 to 2019. The data was collected from the [Data.gov.sg](https://beta.data.gov.sg/collections/352/datasets/d_e25662f1a062dd046453926aa284ba64/view) website.
2. Weather Data
: This API contains the weather conditions in Singapore from 2016 to 2019. The data was collected from the [Data.gov.sg](https://beta.data.gov.sg/collections/1456/datasets/d_91ffc58263cff535910c16a4166ccbc3/view) website.

Because the sources only provided the data at the current time, we set up a script to collect the data from each source  every 15 minutes and saved them each in a pkl file. The file used to collect the data can be found in `data_collection/pklweathertaxi.py`. For redundancy, we made a separate script to sample the data every hour and saved them each to a CSV file. The file used to collect the data can be found in `data_collection/weathertaxi.py`.

The data was collected from 14 March 2024 to 5 April 2024, resulting in a total of over 3.7 million data points. 

## Data Cleaning and Preparation 
Notebook: `Data_Cleaning_And_Preparation.ipynb`
This notebook is responsible for data cleaning and preparation. It provides an overview of the data files used in the project and the date/week ranges that are considered.

As the files are too big to house on github, we have included them as a zip file under `data_cleaning/Data_for_model.zip`. In the zip file, there are 4 CSV files that are used in the project:

- `weather_data_final.csv`: This file contains the "clean" version of the weather data. Although there are some missing values, they were not added since they are not used in the project.

- `taxi_data.csv`: This file contains 3.7 million rows of data related to all taxis, including allocated zones, time, date, and weather.

- `consolidated_taxi.csv`: This file contains data on the count of taxis in the same zone, time, date, and weather.

- `consolidated_taxi_1hour.csv`: This file is similar to `consolidated_taxi.csv`, but the time values are rounded down to the nearest hour. This makes it easier for modeling purposes.

The date/week ranges used in the project are as follows:
- Friday to Thursday
- 15/03 to 21/03
- 22/03 to 28/03
- 29/03 to 04/04

These date ranges cover three weeks' worth of data for analysis and experimentation.

## Exploratory Data Analysis



## References
https://beta.data.gov.sg/collections/1456/datasets/d_91ffc58263cff535910c16a4166ccbc3/view

https://beta.data.gov.sg/collections/352/datasets/d_e25662f1a062dd046453926aa284ba64/view