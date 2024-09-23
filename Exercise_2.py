# Python program for implementation of Quicksort Sort 

import random


def partition(arr, low, high):
    """
    The method to find the correct position of pivot element in the sorted array.
    :param arr: array of integers
    :param low: lower bound of the array
    :param high: high bound of the array
    :return: index of the pivot element in the array
    """
    pivot_idx = random.randrange(low, high + 1)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]

    boundary = low - 1
    for idx in range(low, high):
        if arr[high] > arr[idx]:
            boundary += 1
            arr[idx], arr[boundary] = arr[boundary], arr[idx]

    boundary += 1
    arr[high], arr[boundary] = arr[boundary], arr[high]
    return boundary


# Function to do Quick sort
def quickSort(arr, low, high):
    """
    :param arr: array to be sorted
    :param low: the lowest index in array
    :param high: the highest index in array
    Takes: O(n log(n)) time.
    """
    if low < high:
        boundary = partition(arr, low, high)

        quickSort(arr, low, boundary - 1)
        quickSort(arr, boundary + 1, high)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
