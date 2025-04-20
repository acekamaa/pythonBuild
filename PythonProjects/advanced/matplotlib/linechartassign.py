import matplotlib.pyplot as plt

# Temperature changes during the day (morning, noon, evening, night)
temperature = [15, 25, 20, 10]
time_of_day = ['Morning', 'Noon', 'Evening', 'Night']

# create a line chart
plt.plot(time_of_day, temperature, marker='o', color='blue')
plt.title("Temperature Changes Throughout the Day")
plt.xlabel("Time of Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
