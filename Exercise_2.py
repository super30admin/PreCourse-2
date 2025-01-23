def partition(arr, low, high):
    pivot = arr[low]  
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j


def quickSort(arr, low, high):
    if low < high:
        mid = partition(arr, low, high)
        quickSort(arr, low, mid - 1)
        quickSort(arr, mid + 1, high)


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    print("Original array:", arr)
    quickSort(arr, 0, n - 1)
    print("Sorted array is:")
    print(arr)
