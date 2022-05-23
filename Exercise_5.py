"""
LeetCode: NA
TC/SC - see below
Challenge - what to pass in stack
"""

# Python program for implementation of Quicksort

# TC - O(N), SC- O(1)
# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[l]
    i, j = l, h

    while i < j:
        while i < h and arr[i] <= pivot:
            i += 1
        while j > l and arr[j] > pivot:
            j -= 1
        if i < j:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

    # put pivot in appropriate position making sure all elements smaller are in left and vice versa- swap j and l
    tmp = arr[j]
    arr[j] = arr[l]
    arr[l] = tmp

    # return new pivot position
    return j

# TC - O(N^2) - partioning and stack calls, SC - O(N) - stack
def quickSortIterative(arr, stack):
    while stack:
        (l, h) = stack.pop()
        if l < h:
            partitionPosition = partition(arr, l, h)
            stack.append((partitionPosition + 1, h))
            stack.append((l, partitionPosition - 1))


arr = [10, 7, 8, 9, 1, 5]
stack = [(0, len(arr) - 1)]
quickSortIterative(arr, stack)
print(arr)
