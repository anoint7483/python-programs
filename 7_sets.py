# set is a collection of non-repetive element
# it unordered, unidexed, there is no way to change items in set and it does not contain duplicate values
s = {3,5,6,"16",1,3,6,3,1,5,3}
print(type(s))
print(s)

print(len(s)) # it will return 5

s.remove(6) #updates the set to remove 6 from five elements
print(s)

print(s.pop()) # removes an arbitrary element from the set an return the element removed
print(s)

s.add(34) # T add element in the sets
print(s)

# r={9,22}
# print(r)
print(s.union({9,22})) # This will return the union of two sets
print(s.intersection({5,9,3,22})) # This will return the intersection of two sets

s.clear() # it will empties the set
print(s)