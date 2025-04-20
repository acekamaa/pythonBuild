import matplotlib.pyplot as plt

# Sample data
countries = ['USA', 'Canada', 'Mexico', 'Germany', 'France']
populations = [331, 38, 128, 83, 65]  # in millions

plt.bar(countries, populations, color='grey')
plt.title("Country Populations")
plt.xlabel("Countries")
plt.ylabel("Population (in millions)")
plt.show()