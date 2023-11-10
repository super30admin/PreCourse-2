# Python program for implementation of Quicksort

# This function is same in both iterative and recursive

""" TC-> when its already sorted, o(n^2), else, 0(nlogn)"""
def partition(arr, low, high):
    # write your code here
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    i = i + 1
    temp = arr[high]
    arr[high] = arr[i]
    arr[i] = temp
    return i


def quickSortIterative(arr, l, h):
    # write your code here
    stack = []
    low = 0
    high = len(arr) - 1

    # Initialize the stack with the initial values of low and high
    stack.append((low, high))

    while stack:
        # Pop the top element from the stack
        low, high = stack.pop()

        # Get the partition index
        pivot_index = partition(arr, low, high)

        # If there are elements on the left side of the pivot, push them onto the stack
        if pivot_index - 1 > low:
            stack.append((low, pivot_index - 1))

        # If there are elements on the right side of the pivot, push them onto the stack
        if pivot_index + 1 < high:
            stack.append((pivot_index + 1, high))



arr = [10, 7, 8, 9, 1, 5]
# arr = [100, 67, 81, 80, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
