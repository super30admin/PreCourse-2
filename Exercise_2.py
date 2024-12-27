# Python program for implementation of Quicksort Sort
# T.C : O(NlogN)
# Swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# give you explanation for the approach


def partition(arr, low, high):

    # write your code here

    # select pivot
    pivot = arr[high]

    # smaller element index, ltes call it i
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    # Move pivot after smaller elements and
    # return its position
    swap(arr, i + 1, high)
    return i + 1

    # Function to do Quick sort


def quickSort(arr, low, high):

    # write your code here

    if low < high:

        # pi is the partition return index of pivot
        pi = partition(arr, low, high)

        # Recursion calls for smaller elements
        # and greater or equals elements
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    # Driver code to test above


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
