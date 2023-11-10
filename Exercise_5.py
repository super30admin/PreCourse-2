

"""
Time Complexity : O( n*log(n) )
Not sure
Space Complexity : O(n)
Did this code successfully run on Leetcode : N/A
Any problem you faced while coding this :
"""


# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[l]
    pivot_position = l
    i = l + 1
    j = h

    while i < j:

        while arr[i] <= pivot and i < h:
            i += 1
        while arr[j] > pivot and j > l:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[pivot_position], arr[j] = arr[j], arr[pivot_position]
    return j


def quickSortIterative(arr, l, h):
    '''
    Using stack, In iterative approach, we will store position of left side and right side in stack.
    then we will pop one by one and apply partition function until stack becomes empty. '''

    stack = [None] * (h - l + 1)
    print(stack)

    top = -1

    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0:

        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        pivot = partition(arr, l, h)
        # print(arr[p])

        if pivot - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = pivot - 1

        if pivot + 1 < h:
            top = top + 1
            stack[top] = pivot + 1
            top = top + 1
            stack[top] = h


arr = [10, 7, 8, 9, 1, 5]
print("old array = ", arr)
quickSortIterative(arr, 0, len(arr) - 1)
print("New sorted array = ", arr)
