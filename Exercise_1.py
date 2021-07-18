"""Time Complexity : O(log(n))
Space Complexity : O(log(n)) since recursion is used
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No
"""
# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
  #check is the array is empty or not
  if r >= 1:
    mid = l + (r - 1)//2
    #If element is smaller than mid we search in the first half
    if arr[mid] > x:
      return binarySearch(arr, l, mid - 1, x)
    #If element is greater than mid we search in the last half
    elif arr[mid] < x:
      return binarySearch(arr, mid + 1, r, x)
    #If search element is the middle element itself
    else:
      return mid
  #return -1 if array is empty. Nothing to search
  else:
    return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result) 
else: 
    print("Element is not present in array")
