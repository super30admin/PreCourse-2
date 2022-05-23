"""
Time Complexity : O(n*log(n) )
Space Complexity : O(n)
Did this code successfully run on Leetcode : N/A
Any problem you faced while coding this :
"""


# Python program for implementation of Quicksort Sort

# give you explanation for the approach
def partition(arr, low, high):
    '''
    we find pivot and its location. Elements to left and right of pivot needs to be sorted without being dependent
    on each other.
    '''
    pivot = arr[low]
    pivot_position = low
    i = low + 1
    j = high

    while i < j:

        while arr[i] <= pivot and i < high:
            i += 1
        while arr[j] > pivot and j > low:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[pivot_position], arr[j] = arr[j], arr[pivot_position]
    return j


# Function to do Quick sort 
def quickSort(arr, low, high):
    '''
    find pivot and recursively sort left and right side of pivot
    '''
    if low < high:
        pivot_position = partition(arr, low, high)
        quickSort(arr, low, pivot_position - 1)
        quickSort(arr, pivot_position + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),