# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1

# Time Complexity: O(log(n))
# Space Complexity: O(n)
def binarySearch(arr, l, r, x):

    # write your code here

    left = 0
    right = len(arr) - 1

    for i in range(len(arr)):
        mid = (left+right)//2
        match = arr[mid]

        if (x > match):
            left = mid + 1
        elif x < match:
            right = mid - 1
        else:
            return mid
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
