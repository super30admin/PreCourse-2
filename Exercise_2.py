# Python program for implementation of Quicksort Sort
import random

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# give you explanation for the approach
def partition(arr, low, high):
    # pivot_idx = random.randrange(low, high)
    pivot_idx = low
    pivot = arr[pivot_idx]
    swap(arr, pivot_idx, low)
    curr_idx = high

    while high > low:
        if arr[high] > pivot:
            swap(arr, high, curr_idx)
            high -= 1
            curr_idx -= 1
        elif arr[high] < pivot:
            swap(arr, high, low)
            low += 1
        else: # arr[high] == pivot
            high -= 1

    return curr_idx

# Function to do Quick sort
def quickSort(arr, low, high):
    if high <= low:
        return
    pivot = partition(arr, low, high)
    quickSort(arr, low, pivot - 1)
    quickSort(arr, pivot + 1, high)

# Driver code to test above
# arr = [10, 7, 8, 9, 1, 5]
arr = [10, 7, 8, 9, 1, 5, 7, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i], end=" ")
print()
