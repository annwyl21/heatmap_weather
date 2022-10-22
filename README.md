# heatmap_weather
Heatmap to visualise weather data from London Heathrow

Historic [weather] Station Data is freely available to download from the MET office website here: https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data

1. A heatmap to visualise weather data over the last 70 years at London Heathrow.

![Image - Average Maximum Monthly Temperature Between 1950 And 2020](heathrow_heatmap_1950_2020.png)

2. A heatmap to visualise a decade of total rainfall in mm each month.
![Image - Total Rainfall in mm Over A Specific Decade](heathrow_rainfall_heatmap_decade.png)

3. A heatmap to visualise average daily sunshine hours over 20 years.
![Image - Average Hours of Daily Sunshine Over 20 Years](heathrow_sunshine_heatmap.png)

Instructions for use:
Install the requirements; pandas, matplotlib, seaborn, numpy
1. To generate a heatmap to show the maximum temperatures over the last 70 years, run the code heathrow_weather_heatmap.py, also prints the head of the data to the terminal.

Challenges Overcome:
- Cleaning up the data by skipping the first 6 rows of written explanation of the data, renaming the columns, and removing the # symbol from the sunshine hours from September 2005 onwards. The # denoted use of an alternative sensor.
- Recognising how the numpy data grid generates the data and that January is located in the top left rather than the bottom left.
2. To generate a heatmap to show the monthly total of sunshine hours over a specific decade, run the code heathrow_weather_data_grid.py, also prints the numpy grid to the terminal.

Challenges not overcome:
- In order to use the data I had to manually remove all the data from 2021, stopping the data at December 2020 instead, as this created a column problem.