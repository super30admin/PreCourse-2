## Time Complexity : O(N)
## Space Complexity : O(N)
## Did this code successfully run on Leetcode : Yes
## Any problem you faced while coding this : No
##
##
## Your code here along with comments explaining your approach

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
    if l < h:
        pi = partition(arr, l, h)

        quickSortIterative(arr, l, pi - 1)
        quickSortIterative(arr, pi + 1, h)

