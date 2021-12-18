# Python program for implementation of Quicksort Sort
# Time Complexity: O(n^2)
# Space Complexity: O(log n)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No


# partition chooses a pivot, at the end of the array
# and then goes through all the elements
# swaping them in place as necessary to place all less than or equal elements
# to the left of the pivot, leaving the remaining to the right
def partition(arr, low, high):
    i = low - 1
    p = arr[high]
    for j in range(low, high):
        if arr[j] <= p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# recursively partion and sort the array
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


# Driver code
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
