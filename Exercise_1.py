# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity : o(logn)
# Space Complexity : o(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
  
def binarySearch(arr, l, r, x): 
  # the ranges l and r in which the number is searched for mutually inclusive
  
  # This is Normal Linear Scan 
  # res = -1
  # for i in range(l,r+1):
  #       if arr[i] == x:
  #             res = i
  # return res
  
  #Binary Search below
  # define the lower and upper limits
  lower, upper = l, r
      
  # loop to find the number
  while lower <= upper:     
      # find the middle index
      middle = lower + (upper - lower) // 2
      # check if the element at this index is what we are looking for
      if arr[middle] == x:
          return middle
      else:
          # if the number we are looking for is larger than the number at the middle
          # then what we are looking for is in the right half of the list
          if x > arr[middle]:
              lower = middle + 1 
          # otherwise, the number we are looking for is in the left half of the list
          else:
              upper = middle - 1    
  return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
y = 40
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
result2 = binarySearch(arr, 0, len(arr)-2, y)  #Test Case 2
  
if result != -1: 
    print ("Element is present at index" ,result)  
else: 
    print ("Element is not present in array")

if result2 != -1: 
    print ("Element is present at index" ,result2)  
else: 
    print ("Element is not present in array")
    
# output 
#Element is present at index 3
#Element is not present in array