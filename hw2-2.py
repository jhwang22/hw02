import matplotlib.pyplot as plt


State = ['DC', 'NY', 'HI', 'CA', 'OR', 'WA', 'AK', 'MA', 'NV', 'VT']
Rate = [90.4,46.9,45.6,40.9,34.7,30.1,26.6,26.1,22.4,17.8]

plt.bar(State, Rate)
plt.title('Estimated rate of homelessness in the United States in 2020, by state (per 10,000 population) ')
plt.xlabel('State')
plt.ylabel('Rate')
plt.show()


