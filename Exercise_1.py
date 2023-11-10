# // Time Complexity : O(log)
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode :
# // Any problem you faced while coding this : No


# // Your code here along with comments explaining your approach
"""
1. calculate mid with l and r and check with given number
2. if the given number larger than mid value update l index with mid + 1 to consider right half the array
3. if the given number smaller than mid value update r index with mid - 1 to consider left half the array
"""


# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):
    # write your code here
    while l <= r:
        mid = int((l + r) / 2)
        if arr[mid] == x:
            return mid
        else:
            if x < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 20

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")

