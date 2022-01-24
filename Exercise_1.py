#Time Complexity: O(logn)
#Space Complexity: O(n) as one array is used which is of size n
# This code is checked on python editor and it is working completely.


# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
  if len(arr) == 0:# return -1 if the array is empty
    return -1
  else:
    while(l<=r):
      mid = int((l+r)/2)# calculate mid index and transform in integer

      if(arr[mid]> x): # if the element is less than mid value inside the array
        r = mid-1
      elif(arr[mid]< x):# if the element is greaterthan mid value inside the array
        l= mid+1
      else:
        return mid
  return -1
  
    
  
# Test array 
arr= [ 2, 3, 4, 10, 40 ] 
x = 40
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index", result) #here, thenindex position will be revealed
else: #DElement is not there 
    print("Element is not present in array")


