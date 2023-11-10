# Python code to implement iterative Binary  
# Search. 

 # Time complexity: O(n)
 # Space Complexity:O(n)


# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  l=0
  r= len(arr)-1
  mid=0

  while l<=r:
      mid= r-l//2

      if x< arr[mid]:       # if element is less than mid, then search it only to the left side
          r = mid-1

      elif x> arr[mid]:     # else, if it is greater than mid, search it to the right side
          l= mid+1

      elif x== arr[mid]:    # else, if it is at mid, return mid index
          return mid

      else:                 # if element not found, return -1
          return -1

  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index ",  result)

else: 
    print ("Element is not present in array")
