# import math as mt
# print(mt.sqrt(4))
# print(mt.factorial(4))
# from math import*
# print(sqrt(4))
# print(factorial(4))
# print(5/3)
# print(5//3)

# def count(s):
#     for str in s.split():
#         s = "&".join(str)
#     return s
# print(count("Python is fun to learn."))  

# x = ['12','hello',456]
# x[0]*=3
# x[1][1] = 'bye'




# import numpy as np

# # Create a 1D NumPy array
# arr = np.array([1, 2, 3, 4, 5])

# # Basic operations
# arr_sum = np.sum(arr)        # Sum of all elements
# arr_mean = np.mean(arr)      # Mean of the elements
# arr_squared = np.square(arr) # Squaring each element

# print("Array:", arr)
# print("Sum:", arr_sum)
# print("Mean:", arr_mean)
# print("Squared:", arr_squared)

# import matplotlib.pyplot as plt
# import numpy as np
# # Create data
# x = np.linspace(0,100,1000)
# y = np.sin(x)

# # Create a plot
# plt.plot(x, y, label='Sine Wave')
# plt.title('Simple Sine Wave Plot')
# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')
# plt.legend()

# # Show the plot
# plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a Pandas DataFrame
data = {
    'Time': np.linspace(0, 2*np.pi, 100),
    'Amplitude': np.sin(np.linspace(0, 2*np.pi, 100))
}
df = pd.DataFrame(data)

# Step 2: Analyze the data
mean_amplitude = df['Amplitude'].mean()

# Step 3: Plot the data
plt.plot(df['Time'], df['Amplitude'], label='Sine Wave')
plt.axvline(mean_amplitude, color='r', linestyle='dotted', label='Mean Amplitude')
plt.title('Sine Wave with Mean Amplitude')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

# Step 4: Show the plot
plt.show()

# Print the mean amplitude
print("Mean Amplitude:", mean_amplitude)




