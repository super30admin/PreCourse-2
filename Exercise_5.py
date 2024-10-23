# Python program for implementation of Quicksort
#Time complexity: O(nlogn), partition iterates through n elements and partition will be called logn times at the best case
#No additional space
# This function is same in both iterative and recursive
def partition(arr, low, high):
    # write your code here
    pivot = arr[high]
    left = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
    arr[high], arr[left] = arr[left], pivot
    return left


def quickSortIterative(arr, l, h):
    # write your code here
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot_index = partition(arr, low, high)

            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

    return arr


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5, 6, 13]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
