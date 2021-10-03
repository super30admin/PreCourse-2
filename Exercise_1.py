# Time Complexity : O(log(N))
# Space Complexity : O(1)

# Exercise 1 : Binary Search
# Python code to implement iterative Binary Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  if r >=l:

    #mid element 
    mid = (l + r) //2

    #if the mid element is equal to x, return x
    if arr[mid] == x:
      return mid

    #if x is smaller than mid, then x will be found in left subarray
    elif arr[mid] > x:
      return binarySearch(arr,l,mid-1,x)

    #else if not found anywhere x is in right subarray
    else:
      return binarySearch(arr,mid+1, r, x)

  #if x is not found return -1
  return -1
  
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 2
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" %result) 
else: 
    print ("Element is not present in array")
