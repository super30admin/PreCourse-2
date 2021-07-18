"""Time Complexity : O(nlog(n))
Space Complexity : O(log(n))
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : Yes I confused with visualizing 
recursion and maintaing stack elements
"""
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #store pivot index and initialize pivot
    pivot_index = l
    pivot = arr[l]
    #run loop still low crosses high and when 
    # it happens we swap it with element on higher end
    while l < h:
        #while elements on low index are less than pivot
        #we increment low
        while l < len(arr) and arr[l] <= pivot:
            l += 1
        #while elements on high index are high than pivot
        #we decrement high
        while arr[h] > pivot:
            h -= 1
        #whenever high and low indexes cross each other
        #we swap elements on high and low index with 
        # each other
        if l < h:
            arr[l], arr[h] = arr[h], arr[l]
    #swap pivot with element on high index
    #which puts pivot on correct position
    arr[h], arr[pivot_index] = arr[pivot_index], arr[h]
    return h

def quickSortIterative(arr, l, h):
  # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)
 
    # initialize top 
    top = -1
 
    #initialize l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
 
    # Keep popping from stack while not empty
    while top >= 0:
 
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
 
        # Set pivot element at its correct position in
        # sorted array
        p = partition( arr, l, h )
 
        # Basically what we did in recursive approach,
        # we did p+1 and p-1 and called quickSort.
        # Here we do the same but just by maintaining
        # stack elements in the form of high and low 
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
 
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

