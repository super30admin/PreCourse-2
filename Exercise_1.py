# Time: O(log n); Space: O(1)

def binarySearch(arr, l, r, x):
    """Iteratively return x's index in sorted arr[l:r + 1], or -1 if absent."""
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = binarySearch(arr, 0, len(arr) - 1, x)

    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
