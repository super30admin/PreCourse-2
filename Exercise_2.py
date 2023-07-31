# Python program for implementation of Quicksort Sort
# // Time Complexity : O(nlogn)
# // Space Complexity : O(logn)
# // Did this code successfully run on Leetcode : No
# // Any problem you faced while coding this : No


# // Your code here along with comments explaining your approach

# give you explanation for the approach
def partition(arr, low, high):
    # write your code here
    # set pivot to highest element
    pivot = arr[high]
    # set boundary to -1
    b = low - 1
    # going through each element of array
    for i in range(low, high):
        # if element is smaller than pivot
        if arr[i] <= pivot:
            # increase the boundary
            b += 1
            # swap the smaller number with the boundary element
            arr[i], arr[b] = arr[b], arr[i]
    # after partitioning till second last element putting pivot in its correct position
    arr[b+1], arr[high] = arr[high], arr[b+1]
    return b+1

# Function to do Quick sort


def quickSort(arr, low, high):
    # write your code here
    if low < high:
        pivot_index = partition(arr, low, high)
        # Recursively sort the two sub-arrays
        quickSort(arr, low, pivot_index - 1)
        quickSort(arr, pivot_index + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
