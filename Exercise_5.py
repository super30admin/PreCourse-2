# Python program for implementation of Quicksort Sort (Iterative)
"""
Time Complexity: O(n log n) on average, O(n^2) in worst case (same as recursive version;
median-of-three pivot selection makes the worst case rare in practice).

Space Complexity: O(log n) in the average case, O(log n) in the worst case due to handling how elements 
are pushed onto the stack and not naive implementation.

Did this code successfully run on Leetcode : Yes (Problem: 912. Sort an Array)

Approach:

Same median-of-three pivot selection and Lomuto partitioning as the recursive
version, but recursion is replaced with an explicit stack of (low, high) index
pairs to avoid using the call stack.

After partitioning, instead of pushing both the left and right sub-ranges onto
the stack (which can still lead to O(n) stack depth in worst case),
we compare their sizes:
  - The smaller sub-range is handled by updating (low, high) and looping again
    immediately - no stack push needed.
  - The larger sub-range is pushed onto the stack to be processed later.


"""

def median_of_three(arr, low, high):
    # Sort arr[low], arr[mid], arr[high] in place so arr[mid] ends up the median
    mid = low + (high - low) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    return mid  # Return the index of the median value


def partition(arr, low, high):

    mid = median_of_three(arr, low, high)

    # Swap the median value with the last element to use it as the pivot
    arr[mid], arr[high] = arr[high], arr[mid]
    pivot = arr[high]

    # Standard Lomuto partitioning
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Function to do Quick sort (iterative)
def quickSort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < 0 or high < 0 or low >= high:
        return arr

    stack = [(low, high)]

    while stack:
        low, high = stack.pop()

        # Loop directly on whichever side is smaller, only pushing the larger side.
        while low < high:
            pivot_index = partition(arr, low, high)

            left_size = pivot_index - 1 - low
            right_size = high - (pivot_index + 1)

            if left_size < right_size:
                # Left is smaller: push the larger right side, keep looping on left
                stack.append((pivot_index + 1, high))
                high = pivot_index - 1
            else:
                # Right is smaller (or equal): push the larger left side, keep looping on right
                stack.append((low, pivot_index - 1))
                low = pivot_index + 1

    return arr


def run_tests():
    # Original driver example
    assert quickSort([10, 7, 8, 9, 1, 5]) == [1, 5, 7, 8, 9, 10]

    # Empty array
    assert quickSort([]) == []

    # Single element
    assert quickSort([1]) == [1]

    # Two elements
    assert quickSort([2, 1]) == [1, 2]

    # Already sorted
    assert quickSort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Reverse sorted
    assert quickSort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # All duplicates
    assert quickSort([3, 3, 3, 3]) == [3, 3, 3, 3]

    # Duplicates mixed in
    assert quickSort([4, 2, 2, 8, 4, 1]) == [1, 2, 2, 4, 4, 8]

    # Negative numbers
    assert quickSort([-5, 3, -2, 0, 8, -1]) == [-5, -2, -1, 0, 3, 8]

    # Duplicates + negatives
    assert quickSort([9, -3, 7, 0, 0, -3, 9]) == [-3, -3, 0, 0, 7, 9, 9]

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()

    print("\nDriver code demo:")
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSort(arr, 0, n - 1)
    print("Sorted array is:")
    for i in range(n):
        print("%d" % arr[i])