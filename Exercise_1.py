# Time Complexity : O(logn): It follows Divide and Conquer. Breaks down problem into smaller sub problems
# Space Complexity : O(1)
# Any problem you faced while coding this : Not a challenge as such.

# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):

    # write your code here
    while l <= r:
        mid = (l + r) // 2

        if x > arr[mid]:
            l = mid + 1
        elif x < arr[mid]:
            r = mid - 1
        else:
            return mid

    return -1


# Test array
arr = [2, 3, 4, 10, 40, 100, 900]
x = 90

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index {}".format(result))
else:
    print("Element is not present in array")
