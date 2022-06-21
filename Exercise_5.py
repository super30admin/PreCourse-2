# Time Complexity - O(nlog(n))
# Space Complexity - O(log(n))

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    #write your code here
    # Here, last element of the array has been taken as a pivot element. 
    # And first element of the array as a pointer.
    i = l
    j = h - 1
    pivot = arr[h]
    while i < j:
        while i < h and arr[i] < pivot:
            i += 1

        while j > l and arr[j] >= pivot:
            j -= 1
        # swapping the elements greater than the pivot to the front.
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # At last, swapping the last element with the pointer positioned number.
    if arr[i] > pivot:
        arr[i], arr[h] = arr[h], arr[i]

    return i

def quickSortIterative(arr, l, h):
    #write your code here
    
    size = h - l + 1
    stack = [0] * (size)
    top = -1
    
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    
    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        
        ptr = partition( arr, l, h )        
        
        if ptr - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = ptr - 1
        
        if ptr + 1 < h:
            top = top + 1
            stack[top] = ptr + 1
            top = top + 1
            stack[top] = h
  
