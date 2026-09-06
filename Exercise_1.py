# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
"""
Time Complexity: O(log n) since we are dividing the array into half in each iteration.
Space Complexity: O(1) since we are not using any extra space or any other data structure.

Did this code successfully run on Leetcode : Yes (Problem: 704. Binary Search)
Approach:
1. We will use two pointers left and right to keep track of the current search space.
2. We will calculate the mid index and compare the mid element with the target value x.
3. If the mid element is equal to x, we return the mid index.
4. If the mid element is less than x, we move the left pointer to mid + 1 to search in the right half of the array.
5. If the mid element is greater than x, we move the right pointer to mid - 1 to search in the left half of the array.
6. We repeat steps 2-5 until the left pointer is less than or equal to the right pointer. If we exit the loop without finding x, we return -1 indicating that x is not present in the array.
"""


def binarySearch(arr, l, r, x):

    # write your code here
    # Handling edge cases
    if arr is None or len(arr) == 0:
        return -1
    left = 0
    right = len(arr) - 1
    while left <= right:
        # To avoid integer overflow use left + (right - left) // 2 instead of (left + right) // 2
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def run_tests():
    """A small test suite covering typical, edge, and boundary cases."""

    # 1. Original example: element present in the middle-ish of the array
    arr = [2, 3, 4, 10, 40]
    assert binarySearch(arr, 0, len(arr) - 1, 10) == 3, "element present (10)"

    # 2. Element is the first item
    arr = [2, 3, 4, 10, 40]
    assert binarySearch(arr, 0, len(arr) - 1, 2) == 0, "element is first item"

    # 3. Element is the last item
    arr = [2, 3, 4, 10, 40]
    assert binarySearch(arr, 0, len(arr) - 1, 40) == 4, "element is last item"

    # 4. Element not present (falls between two values)
    arr = [2, 3, 4, 10, 40]
    assert binarySearch(arr, 0, len(arr) - 1, 5) == -1, "element not present (between values)"

    # 5. Element smaller than everything in the array
    arr = [2, 3, 4, 10, 40]
    assert binarySearch(arr, 0, len(arr) - 1, 1) == -1, "element smaller than min"

    # 6. Element larger than everything in the array
    arr = [2, 3, 4, 10, 40]
    assert binarySearch(arr, 0, len(arr) - 1, 100) == -1, "element larger than max"

    # 7. Empty array
    arr = []
    assert binarySearch(arr, 0, -1, 5) == -1, "empty array"

    # 8. None array (edge case handled explicitly in the function)
    assert binarySearch(None, 0, -1, 5) == -1, "None array"

    # 9. Single-element array, element present
    arr = [7]
    assert binarySearch(arr, 0, 0, 7) == 0, "single element, present"

    # 10. Single-element array, element absent
    arr = [7]
    assert binarySearch(arr, 0, 0, 3) == -1, "single element, absent"

    # 11. Two-element array, both possibilities
    arr = [1, 5]
    assert binarySearch(arr, 0, 1, 1) == 0, "two elements, find first"
    assert binarySearch(arr, 0, 1, 5) == 1, "two elements, find second"
    assert binarySearch(arr, 0, 1, 3) == -1, "two elements, not found"

    # 12. Larger array with even length
    arr = list(range(0, 100, 2))  # [0, 2, 4, ..., 98]
    assert binarySearch(arr, 0, len(arr) - 1, 50) == 25, "large even-length array, present"
    assert binarySearch(arr, 0, len(arr) - 1, 51) == -1, "large even-length array, absent (odd number)"

    # 13. Negative numbers
    arr = [-20, -10, -5, 0, 5, 10]
    assert binarySearch(arr, 0, len(arr) - 1, -10) == 1, "negative numbers, present"
    assert binarySearch(arr, 0, len(arr) - 1, -1) == -1, "negative numbers, absent"

    print("All tests passed!")


if __name__ == "__main__":
    # Test array
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = binarySearch(arr, 0, len(arr) - 1, x)

    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")

    print("\nRunning test suite...\n")
    run_tests()