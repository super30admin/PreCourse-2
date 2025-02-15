# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  # loop until left is less than or equal to right
  while (l <= r) :
    # calculate the middle element
    mid = (l+r) // 2
    # check the element at middle index with x. If the values are equal then return x.
    if (arr[mid] == x):
      return mid
    # if the element at middle index is greater than x then it mean x is on left side of the element since the arr is sorted.
    elif (arr[mid] > x):
      # set the right index to mid - 1
      r = mid - 1
    else:
       # else set the left index to mid + 1
       l = mid + 1
    # if the element is not present then return -1
  return -1   
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index % d" % result 
else: 
    print "Element is not present in array"
