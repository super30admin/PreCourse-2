# Python program for implementation of Quicksort

"""
Time Complexity:
partition: O(n)
quickSortIterative: O(n log n) on average, O(n^2) in worst case

Space Complexity:
partition: O(1) as it's in-place
quickSortIterative: O(log n) for the stack
"""

# This function is same in both iterative and recursive
def partition(arr, l, h):
    if l == h:
        return l
    if l > h:
        return

    i = l - 1
    j = l
    pivot = arr[h]
    
    while j <= h - 1:
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
        
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1

def quickSortIterative(arr, l, h):
    stack = [(l, h)]
    
    while stack:
        l, h = stack.pop()
        if l < h:
            p = partition(arr, l, h)
            stack.append((l, p - 1))
            stack.append((p + 1, h))

# Test the implementation
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)
quickSortIterative(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
