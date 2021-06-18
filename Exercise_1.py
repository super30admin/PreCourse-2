# Implement iterative Binary Search. 
# time complexity - O(log n)
# Space complexity - O(1)
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 

  if r >= 1:
    # find the mid element: mid is 1, arr[mid] = 3
    mid = (l + r) // 2  

    # if element is found
    if arr[mid] == x:
      return mid

    # if search element is greater than mid 
    elif x > arr[mid]:
      l = mid + 1
      return binarySearch(arr, l, r, x)
    
    # if search element is lesser than mid 
    else:
      r = mid - 1
      return binarySearch(arr, l, r, x)

  else:
    return -1

  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 40
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result) 
else: 
    print("Element is not present in array")
