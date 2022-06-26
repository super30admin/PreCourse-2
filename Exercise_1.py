# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  low = l
  high = r
  while(low<=high):
    mid = int(low + (high-low)/2)
    if(arr[mid]==x):
      return mid
    elif(x<arr[mid]):
      high = mid -1
    else:
      low = mid+1
  return -1 
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 4
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index {}".format(result))
else: 
    print("Element is not present in array")
