# A list is a container which stores set of values of any data type
list = ["abhi",5,True,"CS",22.26]
print(list)
print(type(list))

# List element can be used by their indexes
print(type(list[0]))
print(type(list[1]))
print(type(list[2]))
print(type(list[4]))

l1 = [13,3,5,1,6]
print(l1)

l1.sort() # Update the list in ascending order
print(l1)

l1.reverse() # update the list in reverse order
print(l1)

l1.append(16) # This will add 16 at the end of the list
print(l1)

l1.insert(4,9) # This will add 9 at the index 4
print(l1)

l1.pop(4) # This will remove the element at the index 4
print(l1)

l1.remove(16) # This will remove 16 from the list
print(l1)

x = sum(l1) # To find the sum of all the numbers in the list
print(x)
