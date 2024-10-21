# // Time Complexity : O(log(n))  Binary search halves the search in every iteration
# // Space Complexity : O(1) does not  require any extra space proportional to input size
# // Did this code successfully run on Leetcode :NA
# // Any problem you faced while coding this :No

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while l <= r: 
    m = (l+r)//2      #find midpoint index for search

    if arr[m] == x:   #check if midpoint is outcome
      return m

    elif arr[m]  < x: #check if mid point is less or more than outcome
      l = m + 1       #new left is now the next term after middle 

    else:             #new right is now preceeding term after middle
       r = m - 1

  return -1
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print(f"Element is present at index {result}") 
else: 
    print("Element is not present in array")
