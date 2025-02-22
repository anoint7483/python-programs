# program for linear search
l1 = [3,13,5,6,9,34,16]
num =int(input("Enter the nuber you want to search\n"))

def lin_search(l1,num):
    for i in range(len(l1)):
        if num==l1[i]:
            print(f"{num} is found at index {i}")
            break
    else:
            print("Element is not found")        

lin_search(l1,num)