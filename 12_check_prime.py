# 4. to find the given number is prime or not
n = int(input("Enter the number\n"))

flag = False
if n==1:
    print(n,"is not a prime number")
elif n>1:
    for i in range(2,n//2):
        if(n%i==0):
            flag = True
            break
    if flag:
        print(n,"is not a prime number")    
    else:
        print(n,"is a prime number")    
else:
    print(n,"is not a prime number")