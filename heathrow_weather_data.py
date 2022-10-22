import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('heathrow_weather_data1.txt', delim_whitespace=True, skiprows=6, header=0, names=['Year', 'Month', 'Mean daily maximum temperature', 'Mean daily minimum temperature', 'Days of air frost', 'Total rainfall\, mm', 'Total sunshine hours'])
df['Total sunshine hours'] = df['Total sunshine hours'].str.replace('#','')
#print(df.head())

sns.set_style("whitegrid")#whitegrid, dark, white, ticks
#sns.set_palette("Spectral")
#palette choices: deep, muted, pastel, bright, dark, and colorblind
#http://colorbrewer2.org 
#ColourBrewer Palettes: 
sns.set_context('paper', font_scale=0.5)#notebook, talk, poster
plt.figure(figsize = (10, 6))

#barplot showing each months temperatures for a specific year
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

Year1950 = df[df.Year == 1950]
Year1975 = df[df.Year == 1975]
Year2000 = df[df.Year == 2000]
Year2020 = df[df.Year == 2020]

ax=plt.subplot(1,4,1)
sns.barplot(data=Year1950, x='Month', y='Mean daily maximum temperature')
plt.title('1950')

ax1=plt.subplot(1,4,2)
sns.barplot(data=Year1975, x='Month', y='Mean daily maximum temperature')
plt.title('1975')

ax2=plt.subplot(1,4,3)
sns.barplot(data=Year2000, x='Month', y='Mean daily maximum temperature')
plt.title('2000')

ax3=plt.subplot(1,4,4)
sns.barplot(data=Year2020, x='Month', y='Mean daily maximum temperature')
plt.title('2020')

plt.subplots_adjust(bottom = 0.2, wspace = 0.4)#wspace = horizontal space between plots, hspace = vertical space between plots, margins are top, bottom, left and right
ax.set_xticks(np.arange(len(months)), labels=months)
ax1.set_xticks(np.arange(len(months)), labels=months)
ax2.set_xticks(np.arange(len(months)), labels=months)
ax3.set_xticks(np.arange(len(months)), labels=months)

plt.show()
