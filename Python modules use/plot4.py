import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import *

fig = plt.figure()
ax = plt.axes(projection = '3d')

food = ['Meat','Banana','Avocados','Sweet Potatoes','Spinach','Watermelon','Coconut water','Beans','Legumes','Tomato'] 
calories = [250,130,140,120,20,20,10,50,40,19]
potassium = [40,55,20,30,40,32,10,26,25,20]
fat = [8,5,3,6,1,1.5,0,2,1.5,2.5]

graph = ax.scatter(calories,potassium,fat, color = 'r', marker = '*')
graph = ax.plot(calories,potassium,fat, color = 'g')

ax.set_xlabel('Calories')
ax.set_ylabel('potassium(mg)')
ax.set_zlabel('fat(g)')

for i in range(len(food)):
    ax.text(calories[i], potassium[i], fat[i], food[i])

plt.show()















# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# # Data
# data = {
#     'food': ['Apple', 'Banana', 'Orange', 'Grapes', 'Strawberry'],
#     'calories': [52, 89, 47, 67, 33],
#     'potassium': [107, 358, 181, 191, 153],
#     'fat': [0.2, 0.3, 0.1, 0.2, 0.3]
# }

# # Extract data for plotting
# calories = data['calories']
# potassium = data['potassium']
# fat = data['fat']
# food_names = data['food']

# # Create a figure and 3D axis
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Plot the data
# scatter = ax.scatter(calories, potassium, fat)

# # Add labels to the axes
# ax.set_xlabel('Calories')
# ax.set_ylabel('Potassium (mg)')
# ax.set_zlabel('Fat (g)')

# # Add food name annotations
# for i in range(len(food_names)):
#     ax.text(calories[i], potassium[i], fat[i], food_names[i])

# # Show the plot
# plt.show()
