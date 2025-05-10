# Python program for implementation of Quicksort
#Time Complexity: O(n long n), worst case O(n^2)
#Space Complexity: O(n) -- Auxiliary stack size

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
    pivot = arr[h]      # Choose the last element as pivot
    i = l - 1           # Pointer for the smaller element

    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[h] = arr[h], arr[i + 1]  # Place pivot in correct position
    return i + 1


def quickSortIterative(arr, l, h):
  #write your code here
  # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * size

    # Initialize top of stack
    top = -1

    # Push initial values of l and h to stack
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    # Keep popping from stack while it's not empty
    while top >= 0:
        # Pop h and l
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        # Partition the array
        p = partition(arr, l, h)

        # If there are elements on the left side of pivot, push left subarray to stack
        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1

        # If there are elements on the right side of pivot, push right subarray to stack
        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]) 

