# File Handling

# File opening, reading and closing
# f = open("C:/Users/pc/Dropbox/PC/Documents/text file.txt","r") # open the file using location in read mode only
# text = f.read() # to read the text from the file
# text = f.read(100) # passing 100 shows that how much character to read
# print(text)
# text1 = f.readlines() # To read a line from the file
# print(text1)
# f.close() # to close the file 


# file writing
# f = open("this.txt","w") # The data will be overwritten in "w" mode anly write mode
# f = open("this.txt","r+") # In "r+" mode firstly the data will be read and then written but not overwritten, for reading and writing both
# f = open("this.txt","a") # I, "a" mode data is written at end of the current text
# f = open("this.txt","w+")
# f = open("this.txt","a+")
# write = "Hi, My name is Abhishek Yadav, i am a software developer"
# f.write(write)
# f = open("this.txt","r")
# text = f.read()
# print(text)
# f.close()


# with statement :- the file will close automatically by using with statement
# with open("this.txt") as f:
#     text = f.read()
#     print(text)


# with open('this.txt', 'r') as file:
#     line = file.readline()
#     print(line)

# import os
# os.path.exists("jaypal.txt")
# size = os.path.getsize("jaypal.txt")    
# print(size)
# os.remove("jaypal.txt")
# x = os.listdir("C:/Users/pc/Dropbox/PC/Documents")
# print(x)


    


# with open('this.txt', 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#        print(line[3].strip())

# with open('this.txt', 'r') as file:
#     lines = file.readlines()  # Read all lines into a list
#     if len(lines) >= 2:  # Check if there are at least 2 lines
#         print(lines[2].strip())  # Print the second line (index 1)
#     else:
#         print("The file has less than 2 lines.")



# f = open("this.txt","w")
# wt = " My name is abhishek yadav, i am a engineer"       
# text = f.write(wt)


# f = open("this.txt","r+")

# position = f.tell()
# print(position)
# f.seek(11)
# position = f.tell()
# print(position)
# f.write("Hello This is")

# f = open("this.txt","r")
# f = open("jaypal.txt","w")
# text = f.read()
# print(text)
