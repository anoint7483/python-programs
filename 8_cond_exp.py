# To find greatest of four number

print("Enter four numbers")

a = input("Enter the first number ")
b = input("Enter the second number ")
c = input("Enter the third number ")
d = input("Enter the fourth number ")

p= int(a)#To change string into integer 
q= int(b)
r= int(c)
s= int(d)

if(p>q and p>r and p>s):
    greatest = p
elif(q>p and q>r and q>s):
    greatest = q
elif(r>p and r>q and r>s):
    greatest = r
else:
    greatest = s    

print("gretest number is %s"%greatest)  



#To check the student is passed or failed by the given condition

p = input("Enter Physics marks\n")
c = input("Enter Chemistry marks\n")
m = input("Enter Maths marks\n")

total = int(p)+int(c)+int(m)

print("Your total marks is %s"%total)
per = total/3
# print("Your percentage is %s"%per)
print("Your percentage is %s"% round(per,2)) # to round of the number upto 2 digit after decimal

if(per>40 and int(p)>33 and int(c)>33 and int(m)>33):
     print("You are passed")
else:
     print("you are failed")



#To check the recieved message is spam message or not
text = input("Enter the text you recieved\n")

t = ["make a lot of money","buy now","subscribe this","click this"]

if(text==t[0] or text== t[1] or text==t[2] or text==t[3]):
    print("this is a spam message")
else:
    print("not a spam")    



# To check given username contain less that 10 character or not
username = input("Enter the username\n")

if(len(username)<10):
    print("yes, it contain less than 10 character")
else:
    print("No,It do not contain less that 10 character")    



# To find the name is present in the list or not
list = ["Abhishek","Akarsh","Adarsh","Anurag","Kartikey"]
name = input("Enter the name\n")

if(name==list[0] or name==list[1] or name==list[2] or name==list[3] or name==list[4] ):
    print("yes, the name is present in the list")
else:
    print("not found")    

         

   
