# Time: O(n log n); Space: O(n)

def mergeSort(arr):
    """Sort arr in place with stable merge sort."""
    if len(arr) < 2:
        return

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    mergeSort(left)
    mergeSort(right)

    # Merge the sorted halves back into the original list.
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def printList(arr):
    print(*arr)


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is:")
    printList(arr)
