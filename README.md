# Predicting Taxi Availability Depending on Weather Conditions

This is a mini-project for SC 1015 (Introduction to Data Science and Artificial Intelligence). Our team's objective is to predict the availability of taxis in Singapore based on weather conditions. 

1. [Data Collection](#data-collection)
2. [Data Cleaning and Preparation](#data-cleaning-and-preparation)
3. [Exploratory Data Analysis](#exploratory-data-analysis)
4. [Model Building and Evaluation](#model-building-and-evaluation)
5. [Conclusion](#conclusion)

## Data Collection

The data was collected from the following sources:
1. Taxi Availability Data
: This API gives access to real-time taxi availability data. Returns location coordinates of all Taxis that are currently available for hire.
. The data was collected from the [Data.gov.sg](https://beta.data.gov.sg/collections/352/datasets/d_e25662f1a062dd046453926aa284ba64/view) website.
2. Weather Data
: This API contains the weather conditions in Singapore for the following 2 hours. The data was collected from the [Data.gov.sg](https://beta.data.gov.sg/collections/1456/datasets/d_91ffc58263cff535910c16a4166ccbc3/view) website.

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
Notebook: `1015_WeatherTaxi_AI.ipynb`
This notebook is used for additional preparation as well as exploratory data analysis (EDA) and machine learning.

We explored the correlations the categorical data had with the `Taxi Available` datapoints.
We also plotted charts for
- Taxis Available vs Time
- Taxis Available vs Weather Forecast
- Taxis Available vs Day of the Week
- Histogram for Taxis Available

Furthermore we implemented label encoding for the `FORECAST` datapoint, grouping the following together:
```
0: ['Fair (Night)', 'Fair (Day)', 'Fair & Warm'],
1: ['Partly Cloudy (Night)', 'Partly Cloudy (Day)', 'Cloudy'],
2: ['Showers', 'Light Showers', 'Thundery Showers', 'Heavy Thundery Showers']
```

## Model Building and Evaluation
Notebook: `1015_WeatherTaxi_AI.ipynb`


### DecisionTreeClassifier for Forecast
We first used a `DecisionTreeClassifier` to classify `Forecast` from the other variables: `AREA, HOUR, DAY, TAXI_AVAILABLE`.

We found that:

- Model has HIGH True Positive Rate for (1)
- HIGH False Positive Rate for (0 and 2)

Thus implying that it just predicts most data as (1).

And that although it has a HIGH score of `0.7940833`, it is unusable to correctly predict Forecast.

### DecisionTreeRegressor for TAXI_AVAILABLE
We then used a DecisionTreeRegressor to predict the value of `TAXI_AVAILABLE` given `AREA, HOUR, DAY, FORECAST`.

We found that
- Model has HIGH R^2 (0-1) value of 0.7593102, indicating good fit.
- Model has HIGH MSE too, this indicates large errors in predictions that R^2 does not pick up.
- It is usable to predict the `TAXI_AVAILABLITY`.
- Based on feature importances, the time of day is most important in predicting `TAXI_AVAILABLITY`


### RandomForestRegressor for TAXI_AVAILABLE
We then used a RandomForestRegressor to predict the value of `TAXI_AVAILABLE` given `AREA, HOUR, DAY, FORECAST`.

We found that
- Model has HIGH R^2 (0-1) value of 0.8219488, indicating good fit.
- Model has HIGH MSE too, this indicates large errors in predictions that R^2 does not pick up.
- It is usable to predict the `TAXI_AVAILABLITY`.
- Based on feature importances, the time of day is most important in predicting `TAXI_AVAILABLITY`
- This model better than Decision Tree Regressor as it has Higher R^2 and Lower MSE.


## Contributions
**Teo Zin Han** - Data Collection and Scraping <br>
**Hashim** - Data Cleaning and Preparation <br>
**Scott** - EDA and Machine Learning <br>

## References
https://beta.data.gov.sg/collections/1456/datasets/d_91ffc58263cff535910c16a4166ccbc3/view

https://beta.data.gov.sg/collections/352/datasets/d_e25662f1a062dd046453926aa284ba64/view