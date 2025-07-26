# Python program for implementation of Quicksort (Iterative)
# Time Complexity :   Average / Best: O(n log n) ,   Worst: O(n^2) — e.g., already sorted data with last-element pivot
# Space Complexity :   O(log n) on average for the explicit stack; O(n) in the worst case (degenerate partitions)
# Did this code successfully run on Leetcode :
#   Yes — this pattern works for problems like “Sort an Array” when adapted.
# Any problem you faced while coding this :
#   - Picking a poor pivot (like always the last element) can lead to O(n^2).
#   - It’s easy to forget to push the correct subarray bounds onto the stack.
#   - Be careful with off-by-one errors when pushing (l, p-1) and (p+1, h).


# This function is same in both iterative and recursive
# Python program for implementation of Quicksort (Iterative)

# This function is same in both iterative and recursive
def partition(arr, l, h):
    """
    Lomuto partition scheme:
    - Choose last element as pivot
    - Put all elements <= pivot to its left
    - Return the final pivot index
    """
    pivot = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quickSortIterative(arr, l, h):
    """
    Iterative QuickSort using an explicit stack to simulate recursion.
    """
    stack = [(l, h)]

    while stack:
        l, h = stack.pop()
        if l < h:
            p = partition(arr, l, h)

            # Push left side
            if p - 1 > l:
                stack.append((l, p - 1))
            # Push right side
            if p + 1 < h:
                stack.append((p + 1, h))


# ---- Driver code ----
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    quickSortIterative(arr, 0, len(arr) - 1)
    print("Sorted array is:")
    print(arr)
