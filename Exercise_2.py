"""
Description:
Quicksort is a divide and conquer algorithm. 
The idea of quicksort is to pick an element as pivot and partition the given array around the picked pivot.
Based on the pivot, the array is partitioned into two sub-arrays.
Quicksort can then recursively sort the sub-arrays.

The approach for partition:
Select the last element as pivot.
Start from the first element and compare with pivot.
We swap the element with the first element if it is smaller than the pivot.
Else we leave it as it is.

Time Complexity for partition: O(n)
Time Complexity for quicksort: O(n log n)(Best Case)
Time Complexity for quicksort: O(n^2)(Worst Case when array is already sorted or reverse sorted)
Space Complexity for quicksort: O(log n)

"""


# Python program for implementation of Quicksort Sort
# give you explanation for the approach
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    while low <= high:
        if arr[low] <= pivot:
            i += 1
            arr[i], arr[low] = arr[low], arr[i]
        low += 1

        arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1


# Function to do Quick sort
def quickSort(arr, low, high):

    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
