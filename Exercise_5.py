# Time complexity: O(n^2) worst case and O(n log n) average case
# Space complexity: O(n)
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  # mark the low element as pivot for partitioning
    pivot = arr[l]
    start, end = l, h
    while start < end:
        # move the start pointer forward as long as the elements are less than/equal to the pivot element
        while start <= end and arr[start] <= pivot:
            start += 1
        # move the end pointer backward as long as the elements are greater than pivot
        while start <= end and arr[end] > pivot:
            end -= 1
        # swap start and end elements
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    # swap the end and the pivot(marked by arr[l])
    arr[end], arr[l] = arr[l], arr[end]
    return end


def quickSortIterative(arr, l, h):
  # use a stack to keep track of the low and high, append given low,high values to the stack
    stack = []
    stack.append((l, h))
    while stack:
        low, high = stack.pop()
        # obtain the partition index
        partitionIndex = partition(arr, low, high)
        # append the low and partitionIndex as the low and high for the left half (call quicksort on the left half)
        if partitionIndex-1 > low:
            stack.append((low, partitionIndex-1))
        if partitionIndex+1 < high:
          # append the partitionIndex and high as the low and high for the right half (call quicksort on the right half)
            stack.append((partitionIndex+1, high))


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print("Sorted array is:")
print(arr)
