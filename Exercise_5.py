# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  # Pick the rightmost element as a pivot from the list
    pivot = arr[h]
    pIndex = l
    for i in range(l, h):
        if arr[i] <= pivot:
            # swap(a, i, pIndex)
            temp = arr[i]
            arr[i] = arr[pIndex]
            arr[pIndex] = temp
            pIndex = pIndex + 1
 
    swap(arr, pIndex, h)
    return pIndex


def quickSortIterative(arr, l, h):
    stack = deque()
    stack.append((l, h))
 
    # loop till stack is empty
    while stack:
 
        l, h = stack.pop()
 
        pivot = partition(arr, l, h)
 
        if pivot - 1 > l:
            stack.append((l, pivot - 1))
 
        if pivot + 1 < end:
            stack.append((pivot + 1, h))

