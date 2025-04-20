import matplotlib.pyplot as plt

# how students spend their time
activities = ['Sleeping', 'Eating', 'Coding', 'Gaming']
hours = [8, 2, 10, 4]

plt.pie(hours, labels=activities, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title("Students' Time Distribution")
plt.show()