# Time Complexity : O(n log n)
# Space Complexity : O(log n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[h]  # take last element as pivot
    i = l - 1  # index of smaller element

    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap

    arr[i + 1], arr[h] = arr[h], arr[i + 1]  # place pivot in correct position
    return i + 1


#write your code here


def quickSortIterative(arr, l, h):
    stack = []

    # Push initial values of l and h
    stack.append((l, h))

    # Keep popping until stack is empty
    while stack:
        l, h = stack.pop()
        if l < h:
            # Partition the array
            p = partition(arr, l, h)

            # If elements exist on left side of pivot, push left side to stack
            if p - 1 > l:
                stack.append((l, p - 1))

            # If elements exist on right side of pivot, push right side to stack
            if p + 1 < h:
                stack.append((p + 1, h))
  #write your code here

