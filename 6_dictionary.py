# Dictionary is  a collection of key value-pair seperated by ':' .
# Dictionaries are mutable, unordered, indexed and cannot contain duplicate keys.
# If the two keys are same then it will return the last key value
d = {"sr":5,
     "name":"Abhishek",
     "branch": "cse", 
     "tup": (3,13,16,1,6), # its value is a tuple
    #   list: {3,5} # its value is a set
     }
print(type(d))
print(d)
print(d["branch"]) # it will print the value stored in the key
print(type(d["tup"])) # it will return the type of value stored in the key
print(type(d["name"]))
# print(type(d[list])) # it return a set class instead the key is a denoted by list
# print(d[list])

# Dictionary methods
print(d.items()) # items() function will return the (key,value) tuples.
print(d.keys()) # keys() function return the list of keys
d.update({"year":2}) # update the dictionary with supplied key value pair
print(d)
print(d.get("name")) # return the value of the specified key