import pandas
import matplotlib.pyplot as plt

# read the .csv file
data = pandas.read_csv('3.1 Environment3.1.1. Meteorological Conditions Statistics3.1.1.1. Temperature (°(...)02_25_2023 17_30_06.csv')

# create a dataframe object containing the data
df = pandas.DataFrame(data)

# calculate the mean of the 'Data' column
mean_temp = df['Data'].mean()

# plot the data
ax = df.plot(x='Year', y='Data', kind='line', title='Spring Temperatures (2005-2018)')

# plot the average line
ax.axhline(y=mean_temp, color='r', linestyle='--', label='Mean Temperature')

# add a label to the y-axis
ax.set_ylabel('Temperature (C)')

# add a legend to the plot
ax.legend()

# display the plot
plt.show()
