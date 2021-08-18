# Time Complexity : O(log n)
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : Couldn't find on Leetcode
# Any problem you faced while coding this : None
# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = (l + r) // 2
        if l == r:      # to get out of the infinite loop when l==r
            l = r + 1

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid

    return -1


# write your code here


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
