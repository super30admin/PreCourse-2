#Space Complexity: O(1)
#Time Complexity: O(log n) ... where n is the number of elements
#The code did run successfully

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  while l <= r:                 #checking for the looping invariant in order to maintain the boundaries for the search
    mid = (l + r)//2            #as the logic is to iterate and look for the middle element
    if arr[mid] < x:            #changing the search scope to right half 
      l = mid               
    elif arr[mid] > x:         #changing the search scope to left half  
      r = mid
    else:
      return mid
  return -1
  

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index",result)
else: 
    print("Element is not present in array")
