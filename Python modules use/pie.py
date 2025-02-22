import matplotlib.pyplot as plt

# Data
labels = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Create a pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=60)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')  

# Adding title
plt.title('Simple Pie Chart')

# Display the plot
plt.show()
