# Space Complexity - using explicit stack than the recursive one, O(N)
# Python program for implementation of Quicksort

def swap(arr, ind1, ind2):
    arr[ind1], arr[ind2] = arr[ind2], arr[ind1]

# This function is same in both iterative and recursive
def partition(arr,low,high):
    pivot = arr[low]
    i, j = low, high
    while i<j:
        while arr[i] <= pivot and i<high:
            i += 1
        while arr[j] > pivot and j>low:
            j -= 1
        if i<j:
            swap(arr, i, j)

    swap(arr, j, low)
    return j

def quickSort(arr,low,high):
    if low<high:
        partition_index = partition(arr, low, high)
        quickSort(arr, low, partition_index-1)
        quickSort(arr, partition_index+1, high)

def quickSortIterative(arr, low, high):
    size = high - low + 1
    stack = [0] * size
    top = -1

    top += 1
    stack[top] = low
    top += 1
    stack[top] = high

    # Keep popping from stack while it's not empty
    while top >= 0:
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1
        pivot = partition(arr, low, high)

        if pivot - 1 > low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = pivot - 1

        if pivot + 1 < high:
            top += 1
            stack[top] = pivot + 1
            top += 1
            stack[top] = high

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 