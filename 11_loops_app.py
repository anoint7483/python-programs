# # 1. To print the table of entered number
# x = input("Enter the number to print table\n")
# y = int(x)
# for i in range(1,11):
#     print(f'''{y} X {i} = {y*i}''')


# # 2. To greet the people in the list whoose name starts with A
# l1 = ["Abhishek","Akarsh","Ishatva","Adarsh","Kartikey"]
# i=0
# for i in range(0,5):
#     print("Good Morning!")
#     if(l1[i].startswith("A")):
#      print(l1[i])


# # print the table of entered number using while loop
# x = input("Enter the number to print table\n")
# y = int(x)
# i=1
# while i<=10:
#     print(f'''{y} X {i} = {y*i}''')
#     i+=1


# # To find the sum of first n natural number
# x = int(input("Enter the number\n"))
# sum = 0
# for i in range(1,x+1):
#     sum = sum+i
# print(sum)  


# # To find the factorial of fiven number
# x = int(input("Enter the number\n"))
# fact = 1
# for i in range(1,x+1):
#     fact = fact*i
# print(fact)    


# # 1. Multiplication table in reverse order
# n = int(input("Enter the number to print table\n"))

# for i in reversed(range(1,11)):
#     print(f'''{n} X {i} = {n*i}''')


# # 1. Multiplication table in reverse order
# n = int(input("Enter the number to print table\n"))

# for i in range(10,0,-1): # range(start,stop,step size)
#     print(f'''{n} X {i} = {n*i}''')