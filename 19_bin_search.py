# binary search
#list should be shorted

# #Using iteration 
# def bin_search(l1,num):
#     low =0
#     high = len(l1)-1
#     mid =0
#     while low<=high:
#         mid = (low +high)//2
#         if num>l1[mid]:
#             low = mid+1
#         elif num<l1[mid]:
#             high = mid-1
#         else:
#             return mid    
#     return -1


#Using recursion
def bin_search(l1,low,high,num):
    if low<=high:
        mid = (low +high)//2
        if num==l1[mid]:
            return mid
        elif num<l1[mid]:
            return bin_search(l1,low,mid-1,num)
        else:
            return bin_search(l1,mid+1,high,num)    
    return -1


l1 = [3,5,6,9,13,16,34]
num = int(input("Enter the number you want to search\n"))
res = bin_search(l1,0,len(l1)-1,num)
if res!=-1:
    print("element is found at index",res)    
else:
    print("element is not found")    