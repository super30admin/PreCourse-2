# Time Complexity: O(n logn)
# Space Complexity: O(logn)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1

def quickSortIterative(arr, l, h):
    stack = [(l, h)]
    while stack:
        l, h = stack.pop()
        pivot_idx = partition(arr, l, h)
        if pivot_idx - 1 > l:
            stack.append((l, pivot_idx - 1))
        if pivot_idx + 1 < h:
            stack.append((pivot_idx + 1, h))