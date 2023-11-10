# Program name - implement iterative Binary search
# Author - Prajakta Pardeshi

# Time complexity for binary search o(log n)
# space complexity o{n}


# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  #write your code here
    mid = 0
    
    while (l <= r):
        mid = (l + r) // 2

        if x == arr[mid]:
            return mid

        if x < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 3
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")