# Predicting Taxi Availability Depending on Weather Conditions

This is a mini-project for SC 1015 (Introduction to Data Science and Artificial Intelligence). Our team's obective is to predict the availability of taxis in Singapore based on weather conditions. 

1. [Data Collection](#data-collection)
2. [Data Preprocessing](#data-preprocessing)
3. [Exploratory Data Analysis](#exploratory-data-analysis)
4. [Model Building](#model-building)
5. [Model Evaluation](#model-evaluation)
6. [Conclusion](#conclusion)

## Data Collection
The data was collected from the following sources:
1. Taxi Availability Data: This dataset contains the availability of taxis in Singapore from 2016 to 2019. The data was collected from the [Data.gov.sg](https://beta.data.gov.sg/collections/352/datasets/d_e25662f1a062dd046453926aa284ba64/view) website.
2. Weather Data: This dataset contains the weather conditions in Singapore from 2016 to 2019. The data was collected from the [Data.gov.sg](https://beta.data.gov.sg/collections/1456/datasets/d_91ffc58263cff535910c16a4166ccbc3/view) website.

Because the sources only provided the data at the current time, we set up a script to collect the data from each source  every 15 minutes and saved them each in a pkl file.  

The data was collected from 14 March 2024 to 5 April 2024. The data was collected every 15 minutes, resulting in a total of over 3.7 million data points.

The script used to scrape the data can be found in `data/cron_task.py`.




## References
https://beta.data.gov.sg/collections/1456/datasets/d_91ffc58263cff535910c16a4166ccbc3/view

https://beta.data.gov.sg/collections/352/datasets/d_e25662f1a062dd046453926aa284ba64/view