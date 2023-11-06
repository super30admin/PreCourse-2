# Python program for implementation of QuickSort

# Time complexity for quick sort is O(n log n) and space complexity is O(n)

# In partition function, we set pivot to right most value in array i.e. 3 in this case from [6, 2, 4, 1, 3]. Initially, left is 0 and right is 4 in this case. Then we loop over the array and if jth value is less than pivot value,
# we swap the jth value with the ith value (previous value) in case of 2 < 3, arr[1] and arr[0] got swapped to get [2, 6, 4, 1, 3] and i gets incremented to 1. [1] at j[3] also gets later in the loop with with i[1] to get
# [2, 1, 4, 6, 3]. Then we move the pivot to i[2] to get [2, 1, 3, 6, 4]. Then, we recursively sort right side array first to make it [2, 1, 3, 4, 6] and then left side to get the output.

# This function is same in both iterative and recursive
def partition(arr, left, right):
    pivot = arr[right]
    i = left

    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    temp = arr[i]
    arr[i] = arr[right]
    arr[right] = temp
    return i


def quickSortIterative(arr, left, right):
    if not arr:
        return

    while left < right:
        pivot = partition(arr, left, right)
        if pivot - left < right - pivot:
            quickSortIterative(arr, left, pivot - 1)
            left = pivot + 1
        else:
            quickSortIterative(arr, pivot + 1, right)
            right = pivot - 1
    return arr


# Code to print the list
def printList(arr):
    if len(arr) > 1:
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()


# driver code to test the above code
if __name__ == '__main__':
    arr = [6, 2, 4, 1, 3]
    print("Given array is", end="\n")
    printList(arr)
    quickSortIterative(arr, 0, len(arr) - 1)
    print("Quick Sorted array is: ", end="\n")
    printList(arr)
