# Time Complexity : depends on the pivot being chosen but average case is O(nlogn)
# Space Complexity : O(logn)
# Did this code successfully run on Leetcode : -
# Any problem you faced while coding this : No

# Python program for implementation of Quicksort Sort


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# give you explanation for the approach
def partition(arr, low, high):
    # write your code here
    # using Lomuto parititon; assuming pivot is at the end
    pivot = arr[high]
    # keeping track of lower elements using i and higher elements between i and j
    # initially assuming elements left to i are smaller than pivot
    i = low - 1

    for index in range(low, high):
        # elements right of i and left of j are higher
        if arr[index] > pivot:
            continue

        i += 1
        swap(arr, i, index)

    # swap pivot with it's correct position
    swap(arr, i + 1, high)
    return i + 1


# Function to do Quick sort
def quickSort(arr, low, high):
    # write your code here
    # needs atleast two elements to sort
    if low >= high:
        return

    # after one parition call, the pivot element is at it's correct place
    partitionIndex = partition(arr, low, high)
    quickSort(arr, low, partitionIndex - 1)
    quickSort(arr, partitionIndex + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
