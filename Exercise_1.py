# Time Complexity: O(log n)
# Space Complexity: O(1)

def binarySearch(arr, l, r, x):
    """
    Perform iterative binary search on the sorted array `arr`.
    
    :param arr: List[int], the sorted array to search in
    :param l: int, the starting index of the search range
    :param r: int, the ending index of the search range
    :param x: int, the target value to search for
    :return: int, the index of `x` if found, otherwise -1
    """
    while l <= r:
        mid = l + (r - l) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # Element is not present in array
    return -1

# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
