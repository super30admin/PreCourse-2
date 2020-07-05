# Python program for implementation of Quicksort Sort

# give you explanation for the approach
def partition(arr, low, high):
    # write your code here
    start = low
    pivot = arr[high]
    for current in range(low, high):
        if arr[current] < pivot:
            arr[start], arr[current] = arr[current], arr[start]
            start = (start + 1)
    arr[start], arr[high] = arr[high], arr[start]
    return start


def quickSort(arr, low, high):
    # write your code here
    if (low < high):
        index = partition(arr, low, high)
        quickSort(arr, low, index-1)
        quickSort(arr, index+1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
