# Python program for implementation of Quicksort Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
arr = quick_sort(arr)
print("Sorted array is:")
for item in arr:
    print(item)
