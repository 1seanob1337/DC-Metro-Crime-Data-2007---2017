# DC Metro Crime Data: 2007 - 2017
Student: Joel P Himes

# Project Goals
- Have homicides increased over this decade?

- Which districts or neighborhoods had the highest number of homicides?

- Is there any correlation between the time of the day and the occurrence of homicides?

- Are homicides more likely to occur with a gun or a knife? 

# Benefit of Exploratory Data Analysis
- DC ranked in the top 10 of homicides per 100k citizens, with 22 over the last 20 years.\
(source: https://www.macrotrends.net/states/district-of-columbia/murder-homicide-rate-statistics)

- Resource allocation and planning for the sustainment of combating homicide.

- Community engagement and collaboration, arming the police force with data-driven decisions for the community.

- Targeted law enforcement strategies.

- Evaluation of crime reduction initiatives; If we can track specific metrics to support initiatives.

# Describing the Dataset
- Dataset has 325340 rows consisting of 30 columns.

- Interesting Features:\
  ‘REPORT_DAT': dtype(‘O’)\
  ‘SHIFT': dtype('O')\
  'OFFENSE': dtype('O')\
  'METHOD': dtype('O')\
  'BLOCK': dtype('O')\
  'DISTRICT': dtype('float64')\
  'WARD': dtype('int64')\
  'NEIGHBORHOOD_CLUSTER': dtype('O')\
  'BLOCK_GROUP': dtype('O')\
  'VOTING_PRECINCT': dtype('O')\
  'START_DATE': dtype('O')\
  'END_DATE': dtype('O')\
  'XBLOCK': dtype('float64')\
  ’YBLOCK': dtype('float64')\
  'year': dtype('int64')\
  'crimetype': dtype(‘O’)

- Categorization of Features:\
  Object/String for most of the dataset.\
  Boolean for optional data.\
  Float64 for coordinates.\
  Int64 for date breakdown.

- Missing Data:\
  Normally distributed across the data set, coming out to roughly 19k out of 343k (less than 5% of the dataset).\
  Resulting in 17k rows removed with a new column count of 325340.\
  Mostly coming from NEIGH_CLUSTER or END_DATE (Offense/Crime not closed).\

- Relation of Features:\
  Found a neutral relationship of features for most of the columns, excluding some of the coordinate-based columns and the time break-out columns.\
  Analysis of the dataset showed a weak (at best) correlation between Time_of_Day, Homicide, and Shift.\
  This was the case even with skewing the results in favor of the ‘Evening / Midnight Shift.'

# Have Homicides Increased Over This Decade?



# Which Districts Or Neighborhoods Had The Highest Number Of Homicides?



# Is There Any Correlation Between The Time Of Day & The Occurrence Of Homicides?



# Are homicides more likely to occur with a gun or a knife?



# Folium Plot? 



# Contact Information

Student: Joel P Himes\
\
GitHub: Joel H\
\
Email: himejoel2107@gmail.com\
\
Link to Repo: https://github.com/joelphimes/DC-Metro-Crime-Data-2007---2017 \
\
Link to Dataset: https://www.kaggle.com/datasets/vinchinzu/dc-metro-crime-data
