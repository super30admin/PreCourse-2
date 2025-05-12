# Python program for implementation of Quicksort
# Time Complexity :
#O(n log n) on average, O(n^2) in the worst case (if array is already sorted in a particular order)
# Space Complexity :
#O(log n) in the best case, O(n) in the worst case (due to stack usage)
#Any problem you faced while coding this :
#Understanding how to simulate recursion using a stack was a little confusing at first.

# This function is used to place the pivot element in the correct position
def partition(arr, l, h):
    pivot = arr[h]  # taking the last element as pivot
    i = l - 1  # index of smaller element

    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            # swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # swap arr[i+1] and arr[h] (or pivot)
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


# This function implements iterative quicksort
def quickSortIterative(arr, l, h):
    stack = []

    # push initial values to stack
    stack.append((l, h))

    while stack:
        l, h = stack.pop()
        p = partition(arr, l, h)

        # push left side to stack if it exists
        if p - 1 > l:
            stack.append((l, p - 1))

        # push right side to stack if it exists
        if p + 1 < h:
            stack.append((p + 1, h))


# Driver code
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print(arr[i], end=" ")

