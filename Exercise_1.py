# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1

'''
Time Complexity - O(log n) [Worst case time complexity]
Space Complexity - O(1) [Since it is iterative binary search, in case of recursive it would be O(log n)]
'''


def binarySearch(arr, l, r, x):

    # Making an assumption that the given array is sorted
    while l <= r:

        mid = l + (r-l) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
