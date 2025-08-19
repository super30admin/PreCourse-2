# Python program for implementation of Quicksort
# Time complexity is O(nlogn) average, however worst case is still O(n^2) if we keep chosing smallest/largest value all the time as the pivot
# Space complexity is O(logn) average and worst O(n)
def quickSortIterative(arr, low, high):
    stack = []
    stack.append((low, high))

    while stack:
        low, high = stack.pop()
        if high - low + 1 <= 1:
            continue

        pivot = arr[high]
        left = low

        for i in range(low, high):
            if arr[i] < pivot:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1
        arr[left], arr[high] = arr[high], arr[left]

        stack.append((low, left - 1))
        stack.append((left+1, high))
    return arr

arr = [10, 7, 8, 9, 1, 5]
print("Before:", arr)
quickSortIterative(arr, 0, len(arr)-1)
print("After: ", arr)