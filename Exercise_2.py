# Python program for implementation of Quicksort Sort

# give you explanation for the approach
def partition(arr, low, high):  # low --> first index, high --> last index
    pivot = arr[high]  # setting the last element as pivot

    p_index = low - 1  # keeping track of index of smaller element

    for i in range(low, high):
        # if current element is smaller than pivot
        if (arr[i] < pivot):
            # increementing the index
            p_index = p_index + 1
            # swapping if the current element is smaller
            arr[p_index], arr[i] = arr[i], arr[p_index]

    # placing smaller elements left of pivot and larger elements to the right of pivot,
    # here we are placing the pivot right after the swapped element
    arr[p_index + 1], arr[high] = arr[high], arr[p_index + 1]
    return p_index + 1

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        p_index = partition(arr, low, high)

        # before and after partitioning of elements
        quickSort(arr, low, p_index - 1)
        quickSort(arr, p_index + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
