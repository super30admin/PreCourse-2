# Python program for implementation of Quicksort
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Did this code successfully run on Leetcode: Yes

from collections import deque


# Same as Exercise 2
def partition(arr, low, high):
    i = low - 1
    p = arr[high]
    for j in range(low, high):
        if arr[j] <= p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# iteratively partion and sort the array using a stack to keep track of indexes
def quicksortiterative(arr, l, h):

    # create stack to store low and high index
    stack = deque()
    stack.append((l, h))

    while stack:
        # get indexes
        l, h = stack.pop()

        # rearrange elements to either side of pivot
        p = partition(arr, l, h)

        # push sublist indexes to stack for elements lesser than pivot
        if p - 1 > l:
            stack.append((l, p - 1))

        # push sublist indexes to stack for elements greater than pivot
        if p + 1 < h:
            stack.append((p + 1, h))


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksortiterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
