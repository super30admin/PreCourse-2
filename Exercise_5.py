# Time Complexity : O(nlogn): It follows Divide and Conquer. Breaks down problem into smaller sub problems
# Space Complexity : O(n) : Please can you explain if this is correct?

# Approach: The partition logic is the same as Exercise 2. For the Iterative, using a stack was a good way to do it.

# From the partition, we get the Pivot. And we know that the Pivot is sorted. So for the next run, we push (Pivot - 1, and left) & (pivot +1, right)

# Python program for implementation of Quicksort
from collections import deque

# This function is same in both iterative and recursive
def partition(arr, l, h):
    # write your code here
    left = l
    right = h
    pivot = arr[l]
    while right >= left:
        while right > left and arr[right] >= pivot:
            right -= 1
        while left < right and arr[left] <= pivot:
            left += 1
        if left == right:
            if arr[left] <= pivot:
                arr[l], arr[left] = arr[left], arr[l]
                pivot = arr[l]
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        right -= 1

    return left


def quickSortIterative(arr, l, h):
    # write your code here
    stack = deque()
    left = l
    right = h

    # Add the Start And End for the first run
    stack.append((l, h))

    # Keep running until there are indices in the Stack
    while stack:
        # Push Start and End run from Stack
        left, right = stack.pop()
        pivot = partition(arr, left, right)

        # Push to Stack if there are elements to the left of the Pivot
        if pivot - 1 > left:
            stack.append((left, pivot - 1))

        # Push to Stack if there are elements to the right of the Pivot
        if pivot + 1 < right:
            stack.append((pivot + 1, right))


# Driver code to test above
arr = [50, 10, 80, 11, 23, 0, 4]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
