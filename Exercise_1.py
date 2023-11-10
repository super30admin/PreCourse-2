# Time Complexity : O(log n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# Python code to implement iterative Binary Search.

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):
    while l <= r:
        # solving the mid value and changing it into integer
        mid = int((l+r)/2)
        # checking if taken x is greater than the mid value, then we will check right side of the list
        if arr[mid] < x:
            l = mid + 1
        # checking if taken x is less than the mid value, then we will check left side of the list
        elif arr[mid] > x:
            r = mid - 1
        # if above conditions are false, then return the mid value as x
        else:
            return mid
    # if x is not in the given list return -1
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 50

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
