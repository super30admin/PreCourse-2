# Python code to implement iterative Binary  
# Search. 

# Overall complexity: 
# Bestcase: O(1)
# Worst case: O(1)
# Average case: O(logn)

# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
  
  
  #write your code here
  # check if end of the list is reached or not
  while l <= r:
    # find the mid point of the list
    mid = (l + r) // 2
    # if the middle element of the list is equal to x
    if arr[mid] == x:
      # return mid index
      return mid
    # if the middle element of the list is greater than x then
    elif arr[mid] > x:
      # update r
      r = mid - 1
    # if the middle element of the list is lesser than x then
    else:
      # update l
      l = mid + 1
  # return -1 if x is not present
  return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index %d" %result)
else: 
    print ("Element is not present in array")
