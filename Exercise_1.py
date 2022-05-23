# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
    #write your code here
  if r >= l:
      mid = l + (r-1)//2

      # If element is present at the middle
      if arr[mid] == x:
        return mid
      # If element is smaller than mid, then it is present in left subarray
      elif arr[mid] > x:
        return binarySearch(arr, l, mid-1, x)
      # Else the element is present in right subarray
      else:
        return binarySearch(arr, mid + 1, r, x)
  else:
      #for element not present in the array
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
