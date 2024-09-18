# Python program for implementation of Quicksort Sort


# give you explanation for the approach
def partition(arr, low, high):
    i = low
    j = high - 1
    pivot = arr[high]

    while i <= j:
        while i <= high and arr[i] < pivot:
            i += 1

        while j >= low and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[high] = arr[high], arr[i]
    return i

    # write your code here


# Function to do Quick sort recursively
def quickSort(arr, low, high):
    if low < high:
        part_pos = partition(arr, low, high)
        # calling quickSort on the arrays that are smaller than the partition
        quickSort(arr, part_pos + 1, high)
        quickSort(arr, low, part_pos - 1)
    # write your code here


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),

# time complexity is 0(n^2)
# space complexity is  O(logn)
