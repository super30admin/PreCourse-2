# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
#space complexity - O(1), time complexity O(log n)
#NO difficulties faced
# first condition on binary search is the given array is always sorted.
def binarySearch(arr, l, r, x): 

  # if the array is empty return -1
  if len(arr) == 0:
      return -1

  #iterate through the loop till lower index is less than highe index
  while l < r:
      #find the mid-point
      mid = (l+r)//2
      # return if the mid-point is the key that's being searched for
      if arr[mid] == x:
          return mid
      # else only search for the half greater than middle element
      elif arr[mid] > x:
          r = mid-1
    # or greater than it
      else:
          l= mid + 1

#if not found return -1
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
