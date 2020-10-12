# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
"""
Time Complexity : O(log n)
Space Complexity : O(1)
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No
Your code here along with comments explaining your approach
"""


def binarySearch(arr, l, r, x):
    """
  As the array is already sorted, we calculate the mid indices of the array, compare it with the target value.
  if it is same, we return it, if target is greater, it will obviously be in the subarray after mid.
  If target is smaller, it will obviously be in the subarray before mid.
    """

       while l <= r:
            mid = (l+r)//2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                l = mid+1
            else:
                r = mid-1
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10


# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
