#python .\heathrow_weather_heatmap_alldata.py 1950 2021 1

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import sys
import time

def cycle_through_years(years):
    for year in years:
        get_data_by_month(year)
    temperature_array.append(december)
    temperature_array.append(november)
    temperature_array.append(october)
    temperature_array.append(september)
    temperature_array.append(august)
    temperature_array.append(july)
    temperature_array.append(june)
    temperature_array.append(may)
    temperature_array.append(april)
    temperature_array.append(march)
    temperature_array.append(february)
    temperature_array.append(january)
    
def get_data_by_month(year):
    num = position +1
    for item in range(1,13):
        dataframe_row = df[(df.Year == year) & (df.Month == item)]
        if item == 1:
            january.append(dataframe_row.iat[0,num])
        elif item == 2:
            february.append(dataframe_row.iat[0,num])
        elif item == 3:
            march.append(dataframe_row.iat[0,num])
        elif item == 4:
            april.append(dataframe_row.iat[0,num])
        elif item == 5:
            may.append(dataframe_row.iat[0,num])
        elif item == 6:
            june.append(dataframe_row.iat[0,num])
        elif item == 7:
            july.append(dataframe_row.iat[0,num])
        elif item == 8:
            august.append(dataframe_row.iat[0,num])
        elif item == 9:
            september.append(dataframe_row.iat[0,num])
        elif item == 10:
            october.append(dataframe_row.iat[0,num])
        elif item == 11:
            november.append(dataframe_row.iat[0,num])
        else:
            december.append(dataframe_row.iat[0,num])

def create_big_heatmap():
    if position == 1:
        sns.heatmap(mean_temp, cmap="seismic", center=10)
    elif position == 2:
        sns.heatmap(mean_temp, cmap="bwr", center=4)
    elif position == 3:
        sns.heatmap(mean_temp, cmap="coolwarm_r")
        #_r to reverse the colours
    elif position == 4:
        sns.heatmap(mean_temp, cmap="Blues")
    else:
        sns.heatmap(mean_temp, cmap="afmhot")

def create_annotated_heatmap():
    if position == 1:
        sns.heatmap(mean_temp, cmap="seismic", center=10, annot=True)
    elif position == 2:
        sns.heatmap(mean_temp, cmap="bwr", center=4, annot=True)
    elif position == 3:
        sns.heatmap(mean_temp, cmap="coolwarm_r", annot=True)
    elif position == 4:
        sns.heatmap(mean_temp, cmap="Blues", annot=True)
    else:
        sns.heatmap(mean_temp, cmap="afmhot", annot=True)

#enter start date and end date within range 1950-2021
start_date = int(sys.argv[1])
end_date = int(sys.argv[2])
#enter the number of the data to view from the explore dictionary
position = int(sys.argv[3])
explore = {1: 'Mean daily maximum temperature', 2: 'Mean daily minimum temperature', 3: 'Days of air frost', 4: 'Total rainfall, mm', 5: 'Total sunshine hours'}

#PROBLEMS TO FIX
#airfrost data starts 1949 - fails
#sunshine data starts 1957 - fails
#and it struggles with the 2021 'provisional data'

#this code reads in the heathrow data from the txt file downloaded from the MET office website
df = pd.read_csv('heathrow_weather_data1.txt', delim_whitespace=True, skiprows=6, header=0, names=['Year',
'Month', 'Mean daily maximum temperature', 'Mean daily minimum temperature', 'Days of air frost', 'Total rainfall, mm', 'Total sunshine hours'])
df['Total sunshine hours'] = df['Total sunshine hours'].str.replace('#','')
print(df.head(10))
print(df.tail(10))

temperature_array = []
january = []
february = []
march = []
april = []
may = []
june = []
july = []
august = []
september = []
october = []
november = []
december = []

#use the user input to generate the array of years selected
years=[]
for year in range(start_date, end_date):
    years.append(year)

#call the function and generate the numpy array
cycle_through_years(years)
mean_temp = np.asarray(temperature_array)
       
#manage the figsize based on the number of years requested
if len(years) > 10:
    fig, ax = plt.subplots(figsize = (9, 3))   
    create_big_heatmap()
else:
    fig, ax = plt.subplots()
    create_annotated_heatmap()
    
#Set the axis labels, rotate, size and alignment of label
#x-axis
ax.set_xticklabels(years)
plt.setp(ax.get_xticklabels(), rotation=45, size=5)
#y-axis
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_yticklabels(months)
plt.setp(ax.get_yticklabels(), rotation=0, size=7) 

the_title = explore[position] #putting the column header into the title
ax.set_title("Heathrow - {t} {s} and {e}".format(t=the_title, s=start_date, e=end_date))
ax.set_xlabel('Time Period {s} to {e}'.format(s=start_date, e=end_date))
ax.set_ylabel('Months')

plt.savefig('heathrow_min_temp_heatmap.png')
plt.show()
