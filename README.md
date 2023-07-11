# DC Metro Crime Data: 2007 - 2017
Student: Joel P Himes

# Project Goals
- Is there any correlation between the time of the day and the occurrence of homicides?

- Have homicides increased over this decade?

- Which wards or neighborhoods had the highest number of homicides?

- Are homicides more likely to occur with a gun or a knife?

- Which ward & police service area has had the highest number of homicides over the last decade?

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
  Really spread to a couple of columns across the data set, reaching roughly 19k out of 343k (less than 5% of the dataset).\
  Resulting in 17k rows removed with a new column count of 325340.\
  Mostly coming from NEIGH_CLUSTER or END_DATE (Offense/Crime not closed).\

- Relation of Features:\
  Found a neutral relationship of features for most of the columns, excluding some of the coordinate-based and time-based columns.\
  Analysis of the dataset showed a weak (at best) correlation between Time_of_Day, Homicide, and Shift.\
  This was the case even with skewing the results favoring the ‘Evening / Midnight Shift.'

# Is there any correlation between the time of the day and the occurrence of homicides?

Answer: Weak (at best) correlation between Time_of_Day, Homicide, and Shift.

<img src="./img/Correlation_Heatmap.png">

# Have homicides increased over this decade?

Answer: Some policing initiatives may have worked at certain times.

<img src="./img/Number_of_Homicides_by_Year_2008 _2017png.png">

# Lay of the Land: 8 Wards, 7 Districts, and 57 PSAs.

<img src="./img/Lay_Of_The_Land_DC.png">

# Which wards or neighborhoods had the highest number of homicides?

Answer: Ward 8 of Police District 7 in the Southeastern (SE) corridor. 

<img src="./img/Number_of_Homicides_by_Ward.png">

# Are homicides more likely to occur with a gun or a knife?

Answer: Compared to other offenses, Homicides were committed roughly 75% of the time with a gun.

<img src="./img/Proportion_of_Offense_by_Method.png">

# Which ward & police service area has had the highest number of homicides over the last decade?

Answer: Ward 8

<img src="./img/Ward_Heatmap.png">

Answer: PSA 604

<img src="./img/PSA_Heatmap.png">

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
