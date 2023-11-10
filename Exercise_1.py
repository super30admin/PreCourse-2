# Time Complexity : O(log(N))
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : No


# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  while l <= r:
    pivot = l + (r - l) // 2 
    #Calculate pivot and avoid overflow issues. However, python does not have overflow issues.
    #This is due to the Arbitrary Precision of Integers in Python. However, in the interview one can talk
    #about how this saves space and reduces the overhead of the code.
    
    if x == arr[pivot]:
      return pivot
    
    if x < arr[pivot]:
      r = pivot - 1
    else:
      l = pivot + 1
    
  
  return -1
  
  #write your code here
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
print(result)

if result != -1: 
    print("Element is present at index % d" % result ) 
else: 
    print("Element is not present in array")
