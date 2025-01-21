# Python program for implementation of Quicksort

"""
Approach --
1. Use stack to push elements from the left and right of pivot respectively
2. Use partition function to swap elements

Time complexity - O(n log n)
Space complexity - O(n)
"""


# This function is same in both iterative and recursive
def partition(arr, l, h):
    # use two pointers
    a = l - 1
    j = arr[h]

    for k in range(l, h):
        # if elements in arr are less than last value of arr (j)
        if arr[k] <= j:
            a += 1
            # swap element
            arr[a], arr[k] = arr[k], arr[a]
    arr[a + 1], arr[h] = arr[h], arr[a + 1]
    return a + 1


def quickSortIterative(arr, l, h):
    # get size of the arr
    a_size = h - l + 1

    # create a stack to push and pop elements
    a_stack = [0] * a_size

    # declare top variable
    top = -1

    # push l, h values into stack
    top += 1
    a_stack[top] = l
    top += 1
    a_stack[top] = h

    while top >= 0:
        # pop h, l values from stack
        h = a_stack[top]
        top -= 1
        l = a_stack[top]
        top -= 1

        # create partition to swap elements
        # set pivot at its correct position
        pi = partition(arr, l, h)

        # push elements to the left side of stack, if there are any elements on left of pivot
        if pi - 1 > l:
            top += 1
            a_stack[top] = l
            top += 1
            a_stack[top] = pi - 1

        # push elements to the right side of stack, if there are any elements on right of pivot
        if pi + 1 < h:
            top += 1
            a_stack[top] = pi + 1
            top += 1
            a_stack[top] = h


if __name__ == '__main__':
    arr = [9, 4, 7, 1, 10, 6, 0]
    n = len(arr)
    quickSortIterative(arr, 0, n - 1)
    print("Sorted list: ")
    for i in range(n):
        print(arr[i])
