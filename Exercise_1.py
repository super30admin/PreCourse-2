#Time Complexity:O(logn)
#Space Complexity:O(n)
#This code is running fine


# Python code to implement iterative Binary
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, u, x):
    while l <= u: #terminate condition
        mid = int((l+u)/2)

        if x == arr[mid]:
            return mid
        elif x > arr[mid]: #moving the lower bound to the 1 index ahead of mid
            l = mid+1
        elif x < arr[mid]: #moving the upper bound to the 1 index lower than mid
            u = mid-1

    return -1

# Test array 
arr = []
x = 12
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" , result)
else: 
    print("Element is not present in array")
