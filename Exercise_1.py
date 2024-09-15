# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
    mid = int((l+r)/2)
    if l==r:
        if arr[mid]==x:
            return mid
        else:
            return -1
    while r>l:
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            return binarySearch(arr,mid+1,r,x)
        else:
            return binarySearch(arr,l,mid-1,x)

  

    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 2
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index {}".format(result))
else: 
    print("Element is not present in array")

# Complexity

# Time Complexity -  Binary Tree Traverse - log(n)
# Space Complexity - o(1) as iam  not using the extra space