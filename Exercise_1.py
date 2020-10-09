#Time Complexity : O(nlogn)
#Space Complexity : O(1)
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No


#Your code here along with comments explaining your approach

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
    # we define the mid point at the center of left and right pointer
    #each step we eliminate one half if our search element is not found in there
    while l <= r: 
        mid = (l + r) // 2
        if arr[mid] < x: 
            l = mid + 1
        elif arr[mid] > x: 
            r = mid - 1
        else: 
            return mid
    return -1
  
# Test array 
arr = [1, 2, 3, 4, 9, 11, 24, 31,10, 40 ] 
x = 11
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result)
else: 
    print ("Element is not present in array")