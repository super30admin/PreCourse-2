# Python code to implement iterative Binary  
# Search. 
#Time Complexity: O(log(n))
#Space Complexity: O(log(n)) for the recursion based call stack
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  if r >= l == 0:
    return -1

  mid = l + (r - l) // 2

  if arr[mid] == x:
    return mid

#Since the array is sorted, elements lesser than the middle element would be on the left, and greater elements on the right
  if arr[mid] >= x:
    return binarySearch(arr, l, mid, x)
  else:
    return binarySearch(arr, mid + 1, r, x)
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
