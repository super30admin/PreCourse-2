
# Python program for implementation of Quicksort Sort
# time complexity: Average case o(nlogn) Worst case O(N^2)
# space complexity: O(1)
# Did this code successfully run on Leetcode : NA
# Any problem you faced while coding this : Yes for finding pivot. But solved it eventually

# give you explanation for the approach
# pivot can be taken anywhere; taking pivot as the last element
def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quickSort(arr, low, partition_index - 1)
        quickSort(arr, partition_index + 1, high)
    else:
        return




# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),