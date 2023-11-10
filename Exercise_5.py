# Python program for implementation of Iterative Quicksort

# Time Complexity : 
# Space Complexity : 
# Did this code successfully run on VScode : Yes
# Any problem you faced while coding this : No

# Partition function with pivot as rightmost element
def partition(arr,l,h):            

    # choosing first element as pivot
    pivot_value = arr[h]

    # Since last element is pivot, array will start at first element and end at last element index before pivot
    left = l
    right = h - 1

    finished = False
    while not finished:

        # As long as there are elements in arr and
        # And value of first element is smaller than last but one element
        # No need to do anything as smaller element is on the left. So just to increment to the next position
        while left <= right and arr[left] <= pivot_value:       
            left = left + 1

        # Same as above, as long as elements greater than pivot are on the right just go the the previous index to compare
        while right >= left and arr[right] >= pivot_value:
            right = right - 1

        # When no more elements to compare, exit loop
        if right < left:
            finished = True

        # First smaller element on right or higher element on the lelft we encouter, 
        # swap values with corresponding right/lelft elements
        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

    # When split point is reached, swap pivot value with the left index value
    temp = arr[h]
    arr[h] = arr[left]
    arr[left] = temp

    return left

# Iterative way to perform quicksort using Stack
def quickSortIterative(arr, l, h):
 
    # Creating an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)
 
    # Top of stack Initializing
    top = -1
 
    # Assigning initial values of l and h in the stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
 
    # As long as stack is not empty, pop h & l from stack
    while top >= 0:

        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
 
        # Setting pivot at the right position
        pivot = partition( arr, l, h )
 
        # Elements on left side of pivot, push to the left side to stack
        if pivot-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
 
        # Elements on right side of pivot, push right side to stack
        if pivot + 1 < h:
            top = top + 1
            stack[top] = pivot + 1
            top = top + 1
            stack[top] = h


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),