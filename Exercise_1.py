# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
  low = 0
  high =r
  mid = (low + high) //2
  if arr[low] == x:
      return low
  if arr[high] == x:
    return high
  if arr[mid] == x:
    return mid
  
  while low!=mid!=high:
    if arr[low] == x:
      return low
    if arr[high] == x:
      return high
    if arr[mid] == x:
      return mid

    if arr[mid] < x:
      low = mid
      mid = (low + high)//2
      continue

    if arr[mid]>x:
      high = mid
      mid = (low + high)//2
      continue
  
  return -1
      
    

  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 100
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index " + str(result) )
else: 
    print("Element is not present in array")
