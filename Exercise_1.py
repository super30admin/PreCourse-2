"""  
 
 Time Complexity : O(nlogn)
 Space Complexity : O(1) 
 Did this code successfully run on Leetcode : Yes
 Any problem you faced while coding this : No


 Your code here along with comments explaining your approach :
 First we're checking the left and right boundaries and if they fall in then we're finding a 
 mid inbetween left and right. Now we're checking if mid has the target element if yes we're returning else
 we're checking if the mid element is greater than the target, if yes then we're moving the right to mid - 1 else we're moving left to
 mid + 1 because binary search can only be apply when all elements are in sorted order.
 
 """

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while l <= r:
    mid = ( l + r ) // 2

    if arr[mid] == x:
       return mid
    elif arr[mid] > x:
       r = mid - 1
    else:
       l = mid+1

  return -1

    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d",result)
else: 
    print("Element is not present in array")
