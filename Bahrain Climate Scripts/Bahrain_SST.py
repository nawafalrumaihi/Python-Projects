import pandas
import matplotlib

# read the .csv file
data = pandas.read_csv('bahrain_sst.csv')

# create a dataframe object containing the data
df = pandas.DataFrame(data)

# plot the data
df.plot(y='Temperature', kind='hist', title='SST in Bahrain in C')

# display the plot
matplotlib.pyplot.show()
