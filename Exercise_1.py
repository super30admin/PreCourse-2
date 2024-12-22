#  Time Complexity : O(log n)
# Space Complexity : O(1)
#  Did this code successfully run on Leetcode : Yes, Leetcod - 704 Binary Search
#  Any problem you faced while coding this : No

# Your code here along with comments explaining your approach:
# I have implemented the binary search algorithm using iterative approach. 
# First, I have calculated the mid point of the array and then checked if the mid point is equal 
# to x. If it is equal then I have returned the mid. 
# If the mid point is less than the x then I have updated the left pointer to mid + 1 
# and if the mid point is greater than the x then I have updated the right pointer to mid - 1. 
# These steps are repeated until the left pointer is less than or equal to the right pointer. 
# If the element is not found then I have returned -1.

# Python code to implement iterative Binary Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
    
    #write your code here                                
    while l <= r:
        mid = (l + r) //2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1
    
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print ("Element is not present in array")
