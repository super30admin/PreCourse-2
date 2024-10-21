# Time Complexity:
#   Best Case: O(n log n) - When the pivot divides the array into nearly equal halves.
#   Average Case: O(n log n) - Similar behavior for average inputs.
#   Worst Case: O(n^2) - When the pivot is always the smallest or largest element.

# Space Complexity: O(n) - Due to the stack used to simulate recursion (in the worst case).

# Did this code successfully run on Leetcode?
# Yes, similar problems with iterative Quick Sort run correctly on Leetcode.

# Any problem you faced while coding this:
# Managing the stack correctly and keeping track of indices was a bit tricky initially.

# Your code here along with comments explaining your approach:
# - **Quick Sort** is a divide-and-conquer algorithm that sorts by partitioning the array.
# - In the **iterative version**, we use a **stack** to avoid recursion.
# - The partition function rearranges elements based on the pivot and returns its index.
# - The stack helps simulate recursion for sorting the left and right partitions iteratively.

def partition(arr, l, h):
    """
    This function partitions the array such that elements smaller than the pivot
    are on the left and elements greater than the pivot are on the right.
    """
    pivot = arr[h]  # Choose the last element as the pivot
    i = l - 1  # Pointer for smaller element

    for j in range(l, h):
        if arr[j] < pivot:
            i += 1  # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    # Place the pivot in the correct position
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1  # Return the pivot index

def quickSortIterative(arr, l, h):
    """
    Iterative implementation of Quick Sort using an auxiliary stack.
    """
    # Create an auxiliary stack to store sub-array indices
    size = h - l + 1
    stack = [0] * size

    # Initialize top of the stack
    top = -1

    # Push initial values of l and h to the stack
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    # Keep popping from stack while it's not empty
    while top >= 0:
        # Pop h and l
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        # Set the pivot element at its correct position
        pivot = partition(arr, l, h)

        # If there are elements on the left side of the pivot, push left side to the stack
        if pivot - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = pivot - 1

        # If there are elements on the right side of the pivot, push right side to the stack
        if pivot + 1 < h:
            top += 1
            stack[top] = pivot + 1
            top += 1
            stack[top] = h

# Driver code to test the above implementation
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    print("Given array is:")
    print(arr)
    quickSortIterative(arr, 0, n - 1)
    print("Sorted array is:")
    print(arr)
