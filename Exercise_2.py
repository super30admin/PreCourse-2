# Python program for implementation of Quicksort Sort
import random

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# give you explanation for the approach
def partition(arr, low, high):
    pivot_idx = random.randrange(low, high)
    # pivot_idx = high
    pivot = arr[pivot_idx]
    swap(arr, pivot_idx, high)
    curr_idx = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            curr_idx += 1
            swap(arr, j, curr_idx)
    curr_idx += 1
    swap(arr, curr_idx, high)
    return curr_idx

# Function to do Quick sort
def quickSort(arr, low, high):
    if low >= high:
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
