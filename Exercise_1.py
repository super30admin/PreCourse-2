# Python code to implement iterative Binary  
# Search. 
  
  # // Time Complexity : O(lg n) where n is the number of elements in the array
  # // Space Complexity : O(lg n) where n is the number of elements in the array 
  # for which recursive calls were made
  # // Did this code successfully run on Leetcode : yes
  # // Any problem you faced while coding this : a little when writing the 'terminating condition'
  # if l > r:
  #       return -1

  # // Your code here along with comments explaining your approach

# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  if l > r:
        return -1
  mid = l + (r-l)//2

  # checks mid and returns index if element is found
  if x == arr[mid]:
        return mid
  # if the element is larger than x, then search in left of mid space
  elif x < arr[mid]:
        return binarySearch(arr,l,mid-1,x)
  # if the element is smaller than x, then search in right of mid space
  else:
        return binarySearch(arr,mid+1,r,x)
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 4
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at ",result,"  index") 
else: 
    print("Element is not present in array")
