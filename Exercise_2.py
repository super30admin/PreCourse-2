# Python program for implementation of Quicksort Sort 

# give you explanation for the approach
"""
    time complexity: O(nlog(n))
    space complexity: O(1)
    quick sort works on divide & conquer principle and the entire implementation depends on the choice of the
    pivot, here I have chosen last element as the pivot for the implementation of the partition function.
"""


def partition(arr, low, high):

    i = low
    j = high-1
    pivot = arr[high]
    while i < j:
        while i < high and arr[i] < pivot:
            i += 1
        while j > low and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[high], arr[i] = arr[i], arr[high]
    return i


# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        position = partition(arr, low, high)
        quickSort(arr, low, position-1)
        quickSort(arr, position+1, high)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
