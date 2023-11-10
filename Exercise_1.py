#Time Complexity : O(logn)
 #Space Complexity : O(1)
 #Did this code successfully run on Leetcode :
 #Any problem you faced while coding this :
 
# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
  #write your code here
  low = l
  high = r
  while low < high:
    mid = (low + high) // 2
    if x == arr[mid]:
      return mid
    elif x < arr[mid]:
      high = mid - 1
    elif x > arr[mid]:
      low = mid + 1
  return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index ",result) 
else: 
    print ("Element is not present in array")
