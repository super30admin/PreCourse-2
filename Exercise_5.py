# Python program for implementation of Quicksort
# // Time Complexity : O(nlogn)
# // Space Complexity : O(n)
# // Did this code successfully run on Leetcode : No
# // Any problem you faced while coding this : No


# // Your code here along with comments explaining your approach


# This function is same in both iterative and recursive
def partition(arr, l, h):
    # write your code here
    # set pivot to highest element
    pivot = arr[h]
    # set boundary to -1
    b = l - 1
    # going through each element of array
    for i in range(l, h):
        # if element is smaller than pivot
        if arr[i] <= pivot:
            # increase the boundary
            b += 1
            # swap the smaller number with the boundary element
            arr[i], arr[b] = arr[b], arr[i]
    # after partitioning till second last element putting pivot in its correct position
    arr[b+1], arr[h] = arr[h], arr[b+1]
    return b+1


def quickSortIterative(arr, l, h):
    # write your code here
    # Create an auxiliary stack
    stack = [(l, h)]
    while stack:
        l, h = stack.pop()
        # Partition the array and get the index of the pivot element
        pivot_index = partition(arr, l, h)
        # If there are elements on the left side of the pivot, add them to the stack
        if pivot_index - 1 > l:
            stack.append((l, pivot_index - 1))

        # If there are elements on the right side of the pivot, add them to the stack
        if pivot_index + 1 < h:
            stack.append((pivot_index + 1, h))
