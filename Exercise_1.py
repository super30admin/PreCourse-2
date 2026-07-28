# Time Complexity: O(log n)
# Space Complexity: O(1)

# Did this code successfully run on LeetCode: Yes

# Any problem you faced while coding this: No major issues

# Approach:
# Binary search works only on a sorted array
# Compare the target with the middle element
# If they match, return the middle index
# If the target is greater, search the right half
# If the target is smaller, search the left half

def binarySearch(arr, l, r, x): 
    while (l <= r):
            m = (l + r) // 2
            if (arr[m] == x):
                return m
            elif (arr[m] < x):
                l = m + 1
            else:
                r = m -1
        
    return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index %d" % result) 
else: 
    print("Element is not present in array")
