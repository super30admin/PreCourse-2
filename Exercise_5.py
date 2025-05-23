# Python program for implementation of Quicksort
# Time complexity - O(n log n)
# Space complexity - O (log n)

# This function is same in both iterative and recursive
def partition(arr,low,high):
    #write your code here
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    t = arr[i + 1]
    arr[i + 1] = pivot
    arr[high] = t
    return i + 1

def quickSortIterative(arr, low, high):
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))
