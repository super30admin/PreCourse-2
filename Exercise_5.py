'''
Time Complexity - 
Average Case - O(nlogn) as we are traversing the whole array and dividing after each iteration
Worst Case - O(n^2) when our array will be sorted and we select smallest or largest indexed element as pivot
Space Complexity - O(logn) as we need a call to stack

'''

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
from re import L


def partition(arr, low, high):
    pivot = arr[high]
    ptr = low
    for i in range(low, high):
        if arr[i] <= pivot:
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    arr[ptr], arr[high] = arr[high], arr[ptr]
    return ptr


def quickSortIterative(arr, low, high):
    stack = []

    stack.append(low)
    stack.append(high)

    while stack:
        stack.pop(0)
        stack.pop(0)
        par_index = partition(arr, low, high)

        if low < par_index-1:
            stack.append(low)
            stack.append(par_index-1)
        if high > par_index+1:
            stack.append(par_index+1)
            stack.append(high)

    # Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
