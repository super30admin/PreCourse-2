#  Time Complexity : O(logN)
#  Space Complexity : O(N)
#  Did this code successfully run on Leetcode : yes
#  Any problem you faced while coding this : No

# Python code to implement iterative Binary  
# Search. 



# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
  if l<=r:
    m = l + ((r-l) // 2)
    if arr[m] == x:
      return m
    if x<arr[m] :
      return binarySearch(arr,l,m-1,x)
    else:
      return binarySearch(arr,m+1,r,x)
  return -1

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index " , result) 
else: 
    print("Element is not present in array")

'''
approch : recursive 
'''