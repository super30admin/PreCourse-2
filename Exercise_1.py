# Python code to implement iterative Binary
# Search.

# Time Complexity : O(log n)
# Space Complexity : O(1) as memory remains constant & doesn't scale with the size of the list
# Did this code successfully run on Leetcode : leetcode 704 , yes
# Any problem you faced while coding this : NA

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):
    # write your code here
    # assuming the list is in descending order
    while l <= r:
        mid = (l+r)//2  # find middle index
        if arr[mid] == x:   # if middle element == x, return index
            return mid
        # if middle element < x(i.e.10), then we need to search in the RHS of the list
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1  # if middle element > x, search in the left side of the list
    return -1   # if element is not present, return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
