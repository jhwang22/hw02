import matplotlib.pyplot as plt 
#plot 1st line
x1 = [2007,2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
y1 = [391401, 386361, 403308, 403543, 392316, 390155, 394698, 401051, 391440, 373571, 360867, 358363]

plt.plot(x1, y1, label = "sheltered")

x2 = [2007,2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
y2 = [255857,253423, 226919, 233534, 231472, 231398, 195666, 175399, 173268, 176357, 190129, 194467]

# plotting line 2 
plt.plot(x2, y2, label = "unsheltered")
plt.xlabel('Year')

# Set the y axis label of the current axis.
plt.ylabel('Homeless population and status')

# Set a title of the current axes.
plt.title('Homelessness Population in U.S.')

# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()