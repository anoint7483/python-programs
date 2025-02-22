# To print the fibonacci series havign forst term 0 and second term 1
def fibo():
    n = int(input("Enter the number of terms "))
    i1 = 0
    i2 = 1
    print(i1)
    print(i2)
    for i in range(2,n):
     next = i1+i2
     print(next)
     i1=i2
     i2=next

fibo()