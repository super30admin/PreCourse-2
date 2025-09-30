# Python program for implementation of Quicksort

# Time Complexity : O(n log n) average, O(n^2) worst case
# Space Complexity : O(log n) to O(n) depending on stack size
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Partition function (same as recursive QuickSort)
def partition(arr, l, h):
    pivot = arr[h]        # choose last element as pivot
    i = l - 1             # index of smaller element

    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


# Iterative QuickSort
def quickSortIterative(arr, l, h):
    # Create an auxiliary stack
    stack = [(l, h)]

    # Keep popping subarrays while stack is not empty
    while stack:
        l, h = stack.pop()
        if l < h:
            # Partition the array
            p = partition(arr, l, h)

            # Push left and right subarrays to stack
            stack.append((l, p - 1))
            stack.append((p + 1, h))

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSortIterative(arr, 0, n - 1)
    print("Sorted array is:")
    print(arr)