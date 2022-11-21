# Time Complexity : Best case O(1) when the element at the mid is the looked up element. Worst case O(log n)
# Space Complexity : O(1) since there is no additional Data structure used.
# Did this code successfully run on Leetcode : Did not try running code on Leetcode as the question is slightly different there.
# Any problem you faced while coding this : No isssues faced

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
  #write your code here
  while l <= r:                       #using two pointers and this condition checks whether the pointers are within the boundary
    m = (l + r)//2                    #we compute mid pointer m 
    
    if arr[m] > x:                    #if element at the index m is greater than x then we need to look left
      r = m - 1                       #hence we change the right pointer to m-1
    elif arr[m] < x:                  #if element at m is less than x then we need to look right
      l = m + 1                       #hence we increment left pointer to m+1
    else:                             
      return m                        #if the value we are looking for is exactly at index m we return m
  return -1                           #if value we are looking of is not in the list we return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10

# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
    print(f"Element is present at index {result}")
else: 
    print("Element is not present in array")