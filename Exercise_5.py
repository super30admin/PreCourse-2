def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSortIterative(arr, low, high):
    stack = []
    stack.append(low)
    stack.append(high)

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

# Driver code
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print(arr[i], end=" ")

