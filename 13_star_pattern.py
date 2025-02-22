# # to print star pattern in half pyramid aligned left
# n = int(input("Enter the number of line\n"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#       print("*", end ="   ") # end is used to print in the same line seprated by what will be in " "
#     print("\n")


# # to print star pattern, half pyramid in reverse aligned left
# n = int(input("Enter the number of line\n"))   
# for i in range(1,n+1):
#     for j in range(n-i):
#       print("*", end ="   ")
#     print("\n")


# to print star pattern in pyramid
n = int(input("Enter the number of line\n"))   
for i in range(1,n+1):
    for j in range(0,n-i):
       print("  ", end = " ")
    for k in range(0,2*i-1):
      print("*", end ="  ")
    print("\n")


