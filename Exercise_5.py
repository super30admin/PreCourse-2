"""
Problem - Implement Quick Sort iteratively
Example - Input - numbers = [10,7,8,9,1,5]
          Output - [1,5,7,8,9,10]
Solution - Quick sort algorithm iteratively. Use partition function with last element as pivot
Time Complexity - Worst case O(n^2),
                  Average case O(n log n), where n is number of elements in the given array
Space Complexity - O(n)
Test Cases - Edge Cases - Empty array, duplicates
             Base Cases - Array with 1 element, sorted input array
             Regular Cases - unsorted array with many elements
"""


# This function is same in both iterative and recursive
def partition(arr, low, high):
    i = low - 1  # index of smaller element
    pivot = arr[high]  # last element as pivot

    for j in range(low, high):
      if arr[j] <= pivot:
          i += 1
          arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Iterative approach for Quick Sort
def quick_sort_iterative(arr, low, high):
    # create a stack
    size = high - low + 1
    stack = [0] * size

    # initialize top of stack
    top = -1

    # Push initial values of low and high to stack
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high

    # Pop from stack till it is not empty
    while top >= 0:
        # Pop high and low
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        # Set pivot element at the correct position in sorted array
        pi = partition(arr, low, high)

        # If elements on left side of pivot, push it to stack
        if pi - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = pi - 1

        # if elements on right side of stack, push it to stack
        if pi + 1 < high:
            top = top + 1
            stack[top] = pi + 1
            top = top + 1
            stack[top] = high


# Driver code
mylist = [12, 11, 13, 5, 6, 7]
n = len(mylist)
print ("Given array is", mylist)
quick_sort_iterative(mylist, 0, n - 1)
print("Sorted array is: ", mylist)
