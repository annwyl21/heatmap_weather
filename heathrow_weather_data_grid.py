import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

start_date = 2000
end_date = 2010

df = pd.read_csv('heathrow_weather_data1.txt', delim_whitespace=True, skiprows=6, header=0, names=['Year', 'Month', 'Mean daily maximum temperature', 'Mean daily minimum temperature', 'Days of air frost', 'Total rainfall\, mm', 'Total sunshine hours'])
df['Total sunshine hours'] = df['Total sunshine hours'].str.replace('#','')
print(df.head())

# sns.set_style("whitegrid")#whitegrid, dark, white, ticks
sns.color_palette("YlGnBu")
#palette choices: deep, muted, pastel, bright, dark, and colorblind
#http://colorbrewer2.org 
#ColourBrewer Palettes: 
sns.set_context('paper', font_scale=0.5)#notebook, talk, poster



months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

years = ['Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10']

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
# Using column 5, rainfall to generate the numpy grid
def month_data(year):
    for item in range(1,13):
        dataframe_row = df[(df.Year == year) & (df.Month == item)]
        if item == 1:
            january.append(dataframe_row.iat[0,5])
        elif item == 2:
            february.append(dataframe_row.iat[0,5])
        elif item == 3:
            march.append(dataframe_row.iat[0,5])
        elif item == 4:
            april.append(dataframe_row.iat[0,5])
        elif item == 5:
            may.append(dataframe_row.iat[0,5])
        elif item == 6:
            june.append(dataframe_row.iat[0,5])
        elif item == 7:
            july.append(dataframe_row.iat[0,5])
        elif item == 8:
            august.append(dataframe_row.iat[0,5])
        elif item == 9:
            september.append(dataframe_row.iat[0,5])
        elif item == 10:
            october.append(dataframe_row.iat[0,5])
        elif item == 11:
            november.append(dataframe_row.iat[0,5])
        else:
            december.append(dataframe_row.iat[0,5])

between_two_years(start_date, end_date)

rainfall = np.asarray(temperature_array)
print(rainfall)

fig, ax = plt.subplots()
im = ax.imshow(rainfall)


# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(years)), labels=years)
ax.set_yticks(np.arange(len(months)), labels=months)

# Set x tick label alignment.
plt.setp(ax.get_xticklabels(), ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations in each box.
for i in range(len(months)):
    for j in range(len(years)):
        text = ax.text(j, i, rainfall[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Total Rainfall in mm Between {s} And {e}".format(s=start_date, e=end_date)) 
fig.tight_layout()
plt.savefig('heathrow_rainfall_heatmap_decade.png')
plt.show()
