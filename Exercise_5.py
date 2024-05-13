# Python program for implementation of Quicksort

# Time Complexity: O(n log n) average case, O(n^2) worst case
# Space Complexity: O(log n) average case, O(n) worst case (due to recursive calls)

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[h]  # Selecting the last element as the pivot
    i = l - 1  # Index of smaller element
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quickSortIterative(arr, l, h):
    stack = [(l, h)]

    while stack:
        l, h = stack.pop()
        if l < h:
            p = partition(arr, l, h)
            stack.append((l, p - 1))
            stack.append((p + 1, h))


# Driver code to test the above functions
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i], end=" ")
