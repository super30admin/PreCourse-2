# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  # assuming the array is already sorted (as in case of binary search questions)
  while l <= r :
    
    midval = l + ((r-l+1) // 2)
    
    if arr[midval] == x:
      # if x is in the middle, return location
      return midval
  
    elif arr[midval] < x:
      # if middle value is less than x -> x lies on the right side 
      # -> set midval+1 as the new l
      l = midval + 1
  
    else:
      # x lies on the left side -> set midval-1 as the new r
      r = midval - 1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result) 
else: 
    print("Element is not present in array")
