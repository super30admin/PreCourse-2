# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
# Time Complexity: O(log n)
# Space Complexity: O(1)
def binarySearch(arr, l, r, x): 
  #write your code here
  while l <= r:
    # Checking the mid of an array
    mid = l + (r - 1) // 2
    
    # Checking if the value to search is in the mid
    if arr[mid] == x:
      return mid
    # if search value is greater - ignore the first half of the array plus the mid
    elif arr[mid] < x:
      l = mid + 1
    #  Else search value is lesser - ignore the second half of the array plus the mid
    else:
      r = mid - 1
  # Search Value not found
  return -1
  
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result)
else: 
    print ("Element is not present in array")
