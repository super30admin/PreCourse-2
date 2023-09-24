# Python program for implementation of Quicksort
# Time complexity: O(n log n)
# space complexity: O(1)
def partition(arr, l, h):
    pivot = arr[h]
    i = l - 1  # Index of the smaller element

    for j in range(l, h):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1

def quickSortIterative(arr, l, h):
    stack = [l, h]

    while stack:
        h = stack.pop()
        l = stack.pop()

        pivot_index = partition(arr, l, h)

        if pivot_index - 1 > l:
            stack.append(l)
            stack.append(pivot_index - 1)

        if pivot_index + 1 < h:
            stack.append(pivot_index + 1)
            stack.append(h)

# Driver code to test the quicksort implementation
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)
    print("Given array is:", arr)
    quickSortIterative(arr, 0, n - 1)
    print("Sorted array is:", arr)

