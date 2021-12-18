# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[h]  # setting the last element as pivot

    p_index = l - 1  # keeping track of index of smaller element

    for i in range(l, h):
        # if current element is smaller than pivot
        if (arr[i] < pivot):
            # increementing the index
            p_index = p_index + 1
            # swapping if the current element is smaller
            arr[p_index], arr[i] = arr[i], arr[p_index]

    # placing smaller elements left of pivot and larger elements to the right of pivot,
    # here we are placing the pivot right after the swapped element
    arr[p_index + 1], arr[h] = arr[h], arr[p_index + 1]
    return p_index + 1

# we will be creating a stack here where the starting and ending indices of an array will be stored
# upon which quicksort will be implemented.
def quickSortIterative(arr, l, h):
    # creating a stack and initializing the top of stack
    stack = [0]*len(arr)
    top = -1

    # pushing the starting values l & h
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    # remove the elements from the stack till the while condition satisfies
    while top > -1:

        # popping l and h values
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # call for the index partition
        p_index = partition(arr, l, h)

        # after index partition push all the smaller elements in the left index and
        # bigger elements in the right index

        if p_index - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p_index - 1

        if p_index + 1 < h:
            top = top + 1
            stack[top] = p_index + 1
            top = top + 1
            stack[top] = h
