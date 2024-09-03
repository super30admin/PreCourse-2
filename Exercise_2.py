def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as the pivot
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i += 1
            # Swap the found smaller element with the element at i
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        # pi is the partitioning index, arr[pi] is now at the right place
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Driver code to test the above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
