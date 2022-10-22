import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

start_date = 1950
end_date = 2021

#heathrow_weather_data1.txt
df = pd.read_csv('heathrow_weather_data1.txt', delim_whitespace=True, skiprows=6, header=0, names=['Year', 'Month', 'Mean daily maximum temperature', 'Mean daily minimum temperature', 'Days of air frost', 'Total rainfall\, mm', 'Total sunshine hours'])
df['Total sunshine hours'] = df['Total sunshine hours'].str.replace('#','')
print(df.head())

sns.set_context('paper', font_scale=0.5)#notebook, talk, poster

#imshow - simple categorical heatmap
months = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']

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

def between_two_years(start, stop):
    for year in range(start, stop):
        month_data(year)
    temperature_array.append(january)
    temperature_array.append(february)
    temperature_array.append(march)
    temperature_array.append(april)
    temperature_array.append(may)
    temperature_array.append(june)
    temperature_array.append(july)
    temperature_array.append(august)
    temperature_array.append(september)
    temperature_array.append(october)
    temperature_array.append(november)
    temperature_array.append(december)
    
def month_data(year):
    for item in range(1,13):
        dataframe_row = df[(df.Year == year) & (df.Month == item)]
        if item == 1:
            january.append(dataframe_row.iat[0,2])
        elif item == 2:
            february.append(dataframe_row.iat[0,2])
        elif item == 3:
            march.append(dataframe_row.iat[0,2])
        elif item == 4:
            april.append(dataframe_row.iat[0,2])
        elif item == 5:
            may.append(dataframe_row.iat[0,2])
        elif item == 6:
            june.append(dataframe_row.iat[0,2])
        elif item == 7:
            july.append(dataframe_row.iat[0,2])
        elif item == 8:
            august.append(dataframe_row.iat[0,2])
        elif item == 9:
            september.append(dataframe_row.iat[0,2])
        elif item == 10:
            october.append(dataframe_row.iat[0,2])
        elif item == 11:
            november.append(dataframe_row.iat[0,2])
        else:
            december.append(dataframe_row.iat[0,2])

between_two_years(start_date, end_date)
mean_temp = np.asarray(temperature_array)

fig, ax = plt.subplots(figsize = (9, 2))
sns.heatmap(mean_temp, cmap="seismic")

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(january)), range(start_date, end_date))
ax.set_yticks(np.arange(len(months)), labels=months)
ax.set_xlabel('Years')
ax.set_ylabel('Months')

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
# for i in range(len(months)):
#     for j in range(start_date, end_date):
#         text = ax.text(j, i, mean_temp[i, j],
#                        ha="center", va="center", color="w")

stop_date = end_date-1
ax.set_title("Heathrow - Average maximum monthly temperatures between {s} and {e}".format(s=start_date, e=stop_date)) 

plt.savefig('heathrow_heatmap_1950_2020.png')
plt.show()