# Python program for implementation of Quicksort Sort

# give your explanation for the approach
def partition(arr, low, high):
    pivot = arr[high]
    # pointer to track pivot position
    pivotIndex = 0
    for i in range(high):
        # swap smaller elements with pointer and move forward
        if arr[i] <= pivot:
            arr[i], arr[pivotIndex] = arr[pivotIndex], arr[i]
            pivotIndex += 1
    # put pivot in the right position
    arr[pivotIndex], arr[high] = arr[high], arr[pivotIndex]
    return pivotIndex


# Function to do Quick sort
def quickSort(arr, low, high):
    # stop when the partition has only one element (low == high)
    # or when empty (low > high) - happens on right most end
    if low >= high:
        return
    partitionIndex = partition(arr, low, high)
    # sort smaller elements
    quickSort(arr, low, partitionIndex - 1)
    # sort bigger elements
    quickSort(arr, partitionIndex + 1, high)
    return arr


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
