# Python code to implement iterative Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(log n)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No


# Assumption: arr is sorted
# This is a recursive implementation
def binarySearch(arr, l, r, x):

    # if left index is greater than the right index, we didn't find the element
    if l > r:
        return -1

    # get middle index of array
    m = (l + r) // 2

    # if x is found in the middle, return index
    if arr[m] == x:
        return m

    # otherwise, if x is greater than the value at middle index,
    # look to the right side of the middle, recursively
    if arr[m] < x:
        return binarySearch(arr, m + 1, r, x)

    # otherwise, if x is less than the value at middle index,
    # look to the left side of the middle, recursively
    if arr[m] > x:
        return binarySearch(arr, l, m - 1, x)


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
