# Python program for implementation of Quicksort


# Time Complexity : O(n log n) 
# Space Complexity: O(n) due to the explicit stack used
# Did this code successfully run on Leetcode: NA
# Any problem you faced while coding this: NA

# Partition function (same as recursive Quick Sort)
def partition(arr, l, h):
    # i tracks the position for elements smaller than pivot
    i = l - 1
    pivot = arr[h]  # pick the last element as pivot

    # move all smaller elements to the left of pivot
    for j in range(l, h):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap

    # put pivot in its correct position
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1

# Main iterative Quick Sort function
def quickSortIterative(arr, l, h):
    # create a stack to simulate recursion
    size = h - l + 1
    stack = [0] * size

    top = -1  # initialize stack top

    # push initial low and high indices
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    # keep processing while stack is not empty
    while top >= 0:
        # pop high and low from stack
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        # partition the current sub-array
        p = partition(arr, l, h)

        # if left part exists, push it to stack
        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1

        # if right part exists, push it to stack
        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  