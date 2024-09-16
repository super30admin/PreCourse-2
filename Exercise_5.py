# Python program for implementation of Quicksort
import random

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot_idx = random.randrange(l, h + 1)
    swap(arr, pivot_idx, h)
    pivot = arr[h]
    curr_idx = l - 1

    for i in range(l, h):
        if arr[i] < pivot:
            curr_idx += 1
            swap(arr, curr_idx, i)

    curr_idx += 1
    swap(arr, curr_idx, h)
    return curr_idx


def quickSortIterative(arr, l, h):
    stack = []
    stack.append((l, h))

    while stack:
        low, high = stack.pop()
        pivot = partition(arr, low, high)
        if pivot + 1 < high:
            stack.append((pivot + 1, high))
        if low < pivot - 1:
            stack.append((low, pivot - 1))


# Driver code to test above
# arr = [10, 7, 8, 9, 1, 5]
arr = [10, 7, 8, 9, 1, 5, 7, 5]
n = len(arr)
quickSortIterative(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i], end=" ")
print()
