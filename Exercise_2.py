# Python program for implementation of Quicksort Sort 

# give you explanation for the approach
def partition(arr, low, high):
    """
        This function takes last element as pivot,
        places the pivot element at its correct
        position in sorted array, and places all
        smaller (smaller than pivot) to left of
        pivot and all greater elements to right
        of pivot
    """
    pivot = arr[high]
    partition_index = low

    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[partition_index] = arr[partition_index], arr[i]
            partition_index += 1

    arr[high], arr[partition_index] = arr[partition_index], arr[high]
    return partition_index


# Function to do Quick sort
def quick_sort(arr, low, high):
    """
        The main function that implements QuickSort()
        arr[] --> Array to be sorted,
        low  --> Starting index,
        high  --> Ending index

        TimeComplexity: O(nlogn) if we have a good pivot
        SpaceComplexity: O(1) because we sort in place
    """
    if low < high:
        partition_index = partition(arr, low, high)
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)


if __name__ == '__main__':
    # Driver code to test above
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quick_sort(arr, 0, n - 1)
    print("Sorted array is:")
    for i in range(n):
        print("%d" % arr[i], end=" "),
