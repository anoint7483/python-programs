# String can be written in single, double or tripple quote.
name = "abhishek"
print(name)
print(name[0:4])
# last index is not included in the string slicing 
print(name[0:4])
print(name[:4]) # it will take 0 as a starting index
print(name[4:]) # it will take last as an end.

print(len(name))
print(name[0:len(name)-2])
# above can also be written as
print(name[0:-2])
print(name[-4:-2]) # it will take [len(name)-4 : len(name)-2]
print(name[ ::2]) # it is like [start:stop:step]
print(name[ 0:7:3]) 

#functions for string
a = len(name) # for finding length of the string
print(a) 

b = name.endswith("ek") # To check it is ends with given character or not
print(b) 

c = name.count("h") # to find number of time given character is occured
print(c)

d = name.capitalize() # It will capitalize the first letter of the string
print(d)


intro = "my name is abhishek yadav"
print(intro)
e = intro.find("yadav") # This will return the first index of the word found. if not found then otherwise -1
print(e)

f = intro.replace("abhishek", "abhi") # To replace the word, old word by new word
print(f)

g = "abhi"
print(''' My name is''',g)

h = intro.replace(" ","") # by using replace we can remove all the spaces from the string
print(h)

p = " "
q = p.isspace() # to check that given string have all white spaces
print(q)

m = "Abhishek  Yadav"
k = m.find("  ")
print(k)

# How to add or concate two strings
x = "jai "
y = "shree "
z = "krishna"

r = y+z # by using '+' operator 
print(r)

s = y.join([x,z]) # by using join function, here y will be in between x and z
print(s)

print("%s%s%s" % (x,y,z)) # by using % operator

t = "{}{}{}".format(x,y,z) # by using format functions
print(t)

print(x,y,z) # by using , opertor

# f-string to concate two string
n = "abhi"
age = 20

intro_ = f"Hello my name is {n} and I am {age} years old"
print(intro_)



