# Python program for implementation of Quicksort
# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
     # Choose the rightmost element as pivot
    pivot = arr[h]
 
    # Pointer for greater element
    i = l - 1
 
    # Traverse through all elements
    # compare each element with pivot
    for j in range(l, h):
        if arr[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (arr[i], arr[j]) = (arr[j], arr[i])
 
    # Swap the pivot element with
    # the greater element specified by i
    (arr[i + 1], arr[h]) = (arr[h], arr[i + 1])
 
    # Return the position from where partition is done
    return i + 1


def quickSortIterative(arr, l, h):
  #write your code here
  # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)
  
    # initialize top of stack
    top = -1
  
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
  
    # Keep popping from stack while is not empty
    while top >= 0:
  
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
  
        # Set pivot element at its correct position in
        # sorted array
        p = partition( arr, l, h )
  
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
  
