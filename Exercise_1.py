# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

"""
Time Complexity: log(n) as the search space is divided into halves every time. 

Space Complexity: constant - O(1) as we aren't using any extra memory, just pointers


"""
def binarySearch(arr, l, r, x): 
  
  #write your code here
  ans = -1
  while l <= r: 
    mid = (l+r) // 2
    
    if arr[mid] == x: 
      ans = mid
      break
    elif arr[mid] < x: 
      l = mid + 1
    else: 
      r = mid - 1
  
  return ans
  
  
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
# arr = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 ] 
# x = 7
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")
