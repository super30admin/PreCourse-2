# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
# // Time Complexity : O(NlogN) since sorting takes NlogN and our search takes O(logN)
# // Space Complexity : O(n) since we are using an array to store elements
# // Did this code successfully run on Leetcode : NA
# // Any problem you faced while coding this : None
def binarySearch(arr, l, r, x): 
  
  #write your code here
  arr.sort()
  if arr[l] == x:
     return l
  elif arr[r] == x:
     return r
  else:
    while l<=r:
      mid = (r+l)//2
      if arr[mid] == x:
         return mid
      elif arr[mid] < x:
         l = mid+1
      elif arr[mid] > x:
         r = mid-1
  
  return -1

    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index ", result)
else: 
    print ("Element is not present in array")
