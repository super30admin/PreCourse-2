# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity : O(log n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes (https://leetcode.com/problems/binary-search/)
# Any problem you faced while coding this : No

def binarySearch(arr, l, r, x): 
    while l <= r:
        mid = l + (r - l) // 2
        
        # If element is present at the middle
        if arr[mid] == x:
            return mid
            
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            r = mid - 1
            
        # Else the element can only be present in right subarray
        else:
            l = mid + 1
    
    # Element is not present in array
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
