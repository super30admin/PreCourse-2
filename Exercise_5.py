# Python program for implementation of Quicksort
'''
TC: O(nlogn) average case; O(n^2) worst case
AS: O(logn) average case; O(n) worst case 
'''


# This function is same in both iterative and recursive
def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap smaller element to correct position
  

    # Swap the pivot element with the element at i+1 so it's in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the partition index


def quickSortIterative(arr, l, h):
  #write your code here

    # Create a stack to simulate recursion
    stack = []

    # Push initial values of l and h to stack
    stack.append((l, h))

    # Pop from stack while it's not empty
    while stack:
        l, h = stack.pop()

        # Partition the array and get pivot index
        p = partition(arr, l, h)

        # If elements on the left side of pivot, push left subarray to stack
        if p - 1 > l:
            stack.append((l, p - 1))

        # If elements on the right side of pivot, push right subarray to stack
        if p + 1 < h:
            stack.append((p + 1, h))