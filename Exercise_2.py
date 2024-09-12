# Python program for implementation of Quicksort Sort
# give you explanation for the approach

"""
1. We will pick start element as pivot
2. Partition: -
    a) Place all elements lesser than pivot to its left and elements greater than pivot to its right
3. QuickSort is called recursively for array left to the pivot, and array right to the pivot
4. Print sorted array
"""


def partition(arr, low, high):
    # write your code here
    position = low

    for i in range(low, high):
        if arr[high] > arr[i]:
            arr[i], arr[position] = arr[position], arr[i]
            position += 1
    arr[position], arr[high] = arr[high], arr[position]

    return position


# Function to do Quick sort 
def quickSort(arr, low, high):
    # write your code here
    if high > low:
        part = partition(arr, low, high)
        quickSort(arr, low, part - 1)
        quickSort(arr, part + 1, high)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i], end=" ")
