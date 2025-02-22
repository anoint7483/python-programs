# Tuple is an immutable data type in python means it cannot change,
# once a tuple is defined then its element cannot be manipulated or altered.
a = () # Empty tuple
print(a)

b= (9,) # Tuple with only one element needs a comma
print(b)
  
tup = (3,5,1,3,16,3,1,16,5,3)
print(tup)

count = tup.count(3) # it will count the number of time a element occur
print(count)

d = tup.index(1) # it will return the first index of element occur
print(d)

