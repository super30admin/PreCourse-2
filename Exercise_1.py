# Python code to implement iterative Binary Search.

# It returns the index of x in the given sorted array arr if present, else returns -1.
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2  # Calculate the middle index.

        # Check if x is present at the middle.
        if arr[mid] == x:
            return mid

        # If x is greater, ignore the left half.
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore the right half.
        else:
            r = mid - 1

    # If the element is not present in the array.
    return -1

# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in the array")

