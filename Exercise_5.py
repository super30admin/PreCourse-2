# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quickSortIterative(arr, l, h):

    stack = []
    

    stack.append((l, h))
    

    while stack:
        l, h = stack.pop()
        

        pi = partition(arr, l, h)
        

        if pi - 1 > l:
            stack.append((l, pi - 1))
        if pi + 1 < h:
            stack.append((pi + 1, h))
arr = [2, 1, 3, 5, 6, 7]
n = len(arr)
print("Given array is:", arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:", arr)
