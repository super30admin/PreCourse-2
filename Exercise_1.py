# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
# Time complecity - O(log n)
# Space complexity - O(log n) # recursive stack
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while l<=r:
  	mid = l + (r-l)//2
  	if arr[mid]==x:		# if the middle number matches the element to be searched.
  		return mid
  	elif arr[mid]<x:	# search the element in the right array.
  		return binarySearch(arr, mid+1, r, x)
  	else:				# search the element in the left array
  		return binarySearch(arr, l, mid-1, x)
  return -1
  

# Space complexity - O(1) 
def iterative_binarySearch(arr, l, r, x): 
  
  #write your code here
  while l<=r:
    mid = l + (r-l)//2
    if arr[mid]==x:   # if the middle number matches the element to be searched.
      return mid
    elif arr[mid]<x:  # search the element in the right array.
      l = mid+1
    else:       # search the element in the left array
      r = mid -1
    
  return -1  
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
