# Python program for implementation of Quicksort
# Time Complexity : O(nlogn)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Ran this in VS Code ide
# Any problem you faced while coding this : No

# Approach - Used a stack to push (low, high) pointer for a context.

# This function is same in both iterative and recursive
def partition(arr, low, high):
    pivot = high
    rp = pivot - 1
    lp = low
    # assert high > low, "incorrect high > low"

    while True:
        while arr[lp] < arr[pivot] and lp < high:
            lp = lp + 1

        while arr[rp] > arr[pivot] and rp > 0:
            rp = rp - 1

        if lp >= rp:
            break
        else:
            arr[lp], arr[rp] = arr[rp], arr[lp]

    arr[lp], arr[pivot] = arr[pivot], arr[lp]
    return lp


def quickSortIterative(arr, l, h):
    # pushed the array limits into the stack as a tuple
    stack = [(l, h)]
    while stack:
        (low, high) = stack.pop()

        partition_index = partition(arr, low, high)
        # push the left subarray limits where elements are lesser than pivot element
        if partition_index - 1 >= low:
            stack.append((low, partition_index-1))

        # push the right subarray limits where elements are greater than pivot element
        if partition_index + 1 < high:
            stack.append((partition_index + 1, high))

    return arr


arr = [80, 90, 70, 60, 50, 40, 30]
# arr = [7, 4, 1, 2, 5, 7, 9]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
