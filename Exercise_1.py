# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

#Time Complexity : O(logN) - where n is no of elems
#Space Complexity: O(1)
def binarySearch(arr, l, r, x):
  assert l <= r < len(arr)
  mid = -1

  while l < r:
    mid = (l + r)//2

    if arr[mid] < x:
      l = mid + 1
    else:
      r = mid

  return mid if arr[mid] == x else -1


  #write your code here
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result) #Added parantheses for Python3 - Remove for python2
else: 
    print ("Element is not present in array")
