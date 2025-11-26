# Python program for implementation of Quicksort Sort


# give you explanation for the approach
def partition(arr, low, high):
    # write your code here
    pivot = arr[high]

    start = low
    for end in range(low, high):
        if arr[end] <= pivot:
            arr[start], arr[end] = arr[end], arr[start]
            start+=1
    arr[start], arr[high] = arr[high], arr[start]
    return start


# Function to do Quick sort
def quickSort(arr, low, high):
    # write your code here
    if low < high:
        index = partition(arr, low, high)
        # Sort left half recursively
        quickSort(arr, low, index - 1)
        # Sort right half recursively
        quickSort(arr, index + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
