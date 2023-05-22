# Python code to implement iterative Binary  
# Search. 
# Submitted by : Aryan Singh_RN12MAY2023
# Time Complexity : O(log n) for binarySearch, O(nlog n) due to sorting
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Not applicable
# Any problem you faced while coding this : No
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  #write your code here
  while (l <= r):
    size = (r - l) + 1
    mid = l + (size // 2)
    if arr[mid] == x:
       return mid
    elif x > arr[mid]:
       l = mid + 1
    elif x < arr[mid]:
       r = mid - 1
  return -1
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")
