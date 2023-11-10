# Python code to implement iterative Binary Search
# Time Complexity : O(log n)
# Space Complexity : O(1)
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):  
  if r >= l:
      mid = (r + l) // 2
      # If element is mid return it
      if arr[mid] == x:
          return mid
      # If element is smaller than mid, we traverse through the left half
      elif arr[mid] > x:
          return binarySearch(arr, l, mid - 1, x)
      # Else the right half
      else:
          return binarySearch(arr, mid + 1, r, x) 
  else:
      # if not present, return -1 
      return -1

arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result)
else: 
    print ("Element is not present in array")
