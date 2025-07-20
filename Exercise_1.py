#Time Complexity :O(logn)
#Space Complexity :O(1)
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : none


#Your code here along with comments explaining your approach

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while l<=r:         # while there are still elements to search
     mid=(l+r)//2     # get the mid index and to get integer values 
     if arr[mid]==x:
        return mid
     elif x>arr[mid]: # if the value is larger than the mid value
        l=mid+1       # change the search window to right 
     else:
        r=mid-1       # change the search window to left
  
  return -1           # having searched all elements and not found

  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result) 
else: 
    print("Element is not present in array")
