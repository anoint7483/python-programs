# import matplotlib.pyplot as plt

# # Data
# x = [5, 7, 8, 7, 2, 17, 2, 9]
# y = [99, 86, 87, 88, 100, 86, 103, 87]

# # Create a scatter plot
# plt.scatter(x, y)

# # Adding title and labels
# plt.title('Simple Scatter Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# # Display the plot
# plt.show()



import matplotlib.pyplot as plt
import numpy as np

# Data: Generating random data
# data = np.random.randn(5,10)
data = np.random.randn(1000)
print(data)

# Create a histogram
plt.hist(data, color='blue')

# Adding title and labels
plt.title('Simple Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Display the plot
plt.show()
