# Python program for implementation of Quicksort Sort

# give you explanation for the approach

'''
Time Complexity - 
Average Case - O(nlogn) as we are traversing the whole array and dividing after each iteration
Worst Case - O(n^2) when our array will be sorted and we select smallest or largest indexed element as pivot
Space Complexity - O(logn) as we need a call to stack

'''


def partition(arr, low, high):
    pivot = arr[high]
    ptr = low
    for i in range(low, high):
        if arr[i] <= pivot:
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    arr[ptr], arr[high] = arr[high], arr[ptr]
    return ptr

# Function to do Quick sort


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        par_index = partition(arr, low, high)
        quickSort(arr, low, par_index-1)
        quickSort(arr, par_index+1, high)
    return arr


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
