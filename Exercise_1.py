# Python code to implement iterative Binary Search.
# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, left, right, x):
    """
    Time Complexity: O(log(n))
    Space Complexity: O(1)
    """
    while left < right:
        m = left + (right - 1) // 2
        if x < arr[m]:
            right = m - 1
        elif x > arr[m]:
            left = m + 1
        else:
            return m
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")
