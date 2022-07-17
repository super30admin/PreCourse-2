# Time Complexity : log(n)
# Space Complexity : O(1)

# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1

# Divide the sorted into 2 havles and then compare the middle element and then iterate on the half
# which could have the element, while doing this iteratively
def binarySearch(arr, l, r, x):
    mid = 0
    while l <= r:
        mid = (r + l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x :
            l = mid + 1
        else:
            r = mid - 1
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
