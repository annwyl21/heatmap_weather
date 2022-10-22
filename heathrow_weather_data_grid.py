import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

start_date = 2000
end_date = 2010

df = pd.read_csv('heathrow_weather_data1.txt', delim_whitespace=True, skiprows=6, header=0, names=['Year', 'Month', 'Mean daily maximum temperature', 'Mean daily minimum temperature', 'Days of air frost', 'Total rainfall\, mm', 'Total sunshine hours'])
df['Total sunshine hours'] = df['Total sunshine hours'].str.replace('#','')
# print(df.head())

# sns.set_style("whitegrid")#whitegrid, dark, white, ticks
sns.set_palette("Spectral")
# #palette choices: deep, muted, pastel, bright, dark, and colorblind
# #http://colorbrewer2.org 
# #ColourBrewer Palettes: 
sns.set_context('paper', font_scale=0.5)#notebook, talk, poster
# plt.figure(figsize = (10, 6))

#imshow - simple categorical heatmap
# vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
#               "potato", "wheat", "barley"]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
#            "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]
years = ['Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10']
# harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
#                     [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
#                     [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
#                     [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
#                     [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
#                     [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
#                     [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])
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
print(mean_temp)

fig, ax = plt.subplots()
im = ax.imshow(mean_temp)


# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(years)), labels=years)
ax.set_yticks(np.arange(len(months)), labels=months)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(months)):
    for j in range(len(years)):
        text = ax.text(j, i, mean_temp[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Average maximum monthly temperatures between {s} and {e}".format(s=start_date, e=end_date)) 
fig.tight_layout()

plt.show()
