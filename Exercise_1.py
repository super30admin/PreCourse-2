# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

#The Iterative approach for this algorithm takes O(1) time complexity.
def binarySearch(arr, l, r, x): 
  
  #write your code here
  #Executing the loop until left is greater then right
  while l <=r:
    
    #mid value is the average of left and right most positions
    mid = l + (r-1) //2

    #if x is present at mid position
    if arr[mid] == x:
      return mid
      
    #if x is greater than mid position value
    elif arr[mid] < x:
      l = mid+1
    
    #if x is lesser than mid position value
    else:
      r = mid -1

  #the x value not present ,return -1
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
