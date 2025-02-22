# Program for bubble sort
# correction required--
def print_list(l1):
    for i in range(len(l1)):
        print(l1[i],end ="  ")
    print("\n")

def swap(n1,n2):
    temp = n1
    n1=n2
    n2=temp
    return n1,n2

def bubble_sort(l1):
    for i in range(len(l1)):
        for j in range(len(l1)-1):
            if l1[j]>l1[j+1]:
                print(swap(l1[j],l1[j+1]))  
    return l1                

l1 = [3,13,5,6,9,34,16]
print("The unsorted list is")
print_list(l1)
print("The sorted list is")
bubble_sort(l1)
print_list(l1)


        