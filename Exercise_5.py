# Python program for implementation of Quicksort
def partition(arr, l, h):
    i = (l - 1)
    pivot = arr[h]
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quick_sort_iterative(arr, l, h):
    if l < h:
        pivot = partition(arr, l, h)
        quick_sort_iterative(arr, l, pivot - 1)
        quick_sort_iterative(arr, pivot + 1, h)


array = [5, 2, 23, 6, 7, 12, 1, 2]
print('Unsorted array:{}'.format(array))
quick_sort_iterative(array, 0, len(array) - 1)
print('Sorted array:{}'.format(array))
