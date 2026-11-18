# Time: O(n log n) average, O(n^2) worst; Space: O(log n) average recursion

def partition(arr, low, high):
    """Place the last-element pivot and return its final index."""
    pivot = arr[high]
    boundary = low - 1
    for current in range(low, high):
        if arr[current] <= pivot:
            boundary += 1
            arr[boundary], arr[current] = arr[current], arr[boundary]
    arr[boundary + 1], arr[high] = arr[high], arr[boundary + 1]
    return boundary + 1


def quickSort(arr, low, high):
    """Sort arr[low:high + 1] in place using recursive quicksort."""
    if low < high:
        pivot_index = partition(arr, low, high)
        quickSort(arr, low, pivot_index - 1)
        quickSort(arr, pivot_index + 1, high)


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    quickSort(arr, 0, len(arr) - 1)
    print("Sorted array is:")
    print(*arr)
