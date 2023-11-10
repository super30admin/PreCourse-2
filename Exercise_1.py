# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  # Time O(logN)
  # space O(1)
  #write your code here
  for i in range(r):
    if arr[i] > arr[i+1]:
      print("Arr is not sorted")
      return -1
  while l <= r:
    mid = (l+r)//2
    if x < arr[mid]:
      r = mid
    elif x > arr[mid]:
      l = mid+1
    elif x == arr[mid]:
      return mid
  return -1
    
# Test array 
arr = [ 2, 3, 4, 10, 40, 50, 55, 60, 100, 101 ] 
for i in arr:
    
  # Function call 
  result = binarySearch(arr, 0, len(arr)-1, i) 
    
  if result != -1: 
      print("Element is present at index % d" % result )
  else: 
      print ("Element is not present in array")
