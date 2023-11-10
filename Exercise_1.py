# complexity of this algorithm is O(log n) 
# we are not using extra space so space complexity is O(1)
# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
  if r>=l:
    mid = (r+l)//2
    if arr[mid] == x:
      return mid
    elif arr[mid] > x:
      return binarySearch(arr, l, mid-1, x)
    else:
      return binarySearch(arr, mid+1, r, x)

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != None: 
    print("Element is present at index",result)
else: 
    print("Element is not present in array")
