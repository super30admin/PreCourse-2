# Time complexity = O(nlogn) space complexity = O(n)
# Python program for implementation of Quicksort


# This function is same in both iterative and recursive
def partition(arr, low, high):
    # write your code here
    i, j = low, high
    pivot = arr[low]

    while i < j:

        while arr[i] <= pivot and (
            i < high
        ):  # loop while we get left element greater than pivot
            i += 1

        while arr[j] > pivot and (
            j >= low
        ):  # loop while we get right element smalle than pivot
            j -= 1
        if i < j:
            (arr[i], arr[j]) = (arr[j], arr[i])  # swap arr[i] and arr[j]
    (arr[low], arr[j]) = (arr[j], arr[low])  # swap pivot element with position j
    return j


def quickSortIterative(arr, low, high):
    # write your code here
    #  Initialize stack
    size = high - low + 1
    stack = [0] * (size)
    top = 0
    stack[top] = low
    top += 1
    stack[top] = high

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop high and low
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        # sorted array
        j = partition(arr, low, high)

        # push left side to stack
        if j - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = j - 1

        #  push right side to stack
        if j + 1 < high:
            top = top + 1
            stack[top] = j + 1
            top = top + 1
            stack[top] = high


arr = [4, 3, 5, 2, 1, 3, 2, 3]
print("Given array is", end="\n")
print(arr)
quickSortIterative(arr, 0, len(arr) - 1)
print("Sorted array is: ", end="\n")
print(arr)
