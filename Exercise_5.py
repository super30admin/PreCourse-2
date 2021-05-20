# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
# Time Complexity: nlog(n)
# Space Complexity : O(1)
def partition(arr,low,high):

    index = low
    pivot = arr[index]

    while low < high:

        while low < len(arr) and arr[low] <= pivot:
            low += 1
    
        while arr[high] > pivot:
            high -= 1

        if low < high:
            arr[low], arr[high] = arr[high], arr[low]

    arr[index], arr[high] = arr[high], arr[index]

    return high

# We use an auxiliary stack to find correct index of the pivot using partition function. 
# We push indexes into the stack on which we call the partition function to find correct index 
# of the desried pivot until the stack gets empty.

def quickSortIterative(arr, l, h):
  
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
  
# Driver code to test above
arr = [4, 3, 5, 2, 1, 3, 2, 3]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
    print ("% d" % arr[i], end = " ")
print()
