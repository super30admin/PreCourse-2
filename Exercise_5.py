# Python program for implementation of Quicksort

# Time Complexity : O(N LOGN )
# Space Complexity : O(1)

# This function is same in both iterative and recursive
def partition(arr, l, h):
  # write your code here
    i = l
    j = h
    t = 0
    v = 0
    pivotElement = arr[l]

    while (i < j):
        while (arr[i] <= pivotElement and i <= h - 1):
            i = i+1
        while (arr[j] > pivotElement and j >= l + 1):
            j = j-1

        if (i < j):
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t

    v = arr[l]
    arr[l] = arr[j]
    arr[j] = v
    return j


def quickSortIterative(arr, l, h):
  # write your code here
    arr2 = []
    arr2.append((l, h))

    while arr2:
        low, high = arr2.pop()
        if (low < high):
            pivotIndex = partition(arr, low, high)
            arr2.append((low, pivotIndex-1))
            arr2.append((pivotIndex+1, high))


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i], end=" "),
