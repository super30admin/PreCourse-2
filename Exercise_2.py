# Time Complexity:
#   Best Case: O(n log n) - When the partition process divides the array into two almost equal halves.
#   Average Case: O(n log n) - Typical performance on random data.
#   Worst Case: O(n^2) - When the pivot element divides the array into two highly unbalanced partitions (e.g., already sorted data with a bad pivot).

# Space Complexity: O(log n) - For the recursive stack in the best/average cases; O(n) in the worst case.

# Did this code successfully run on Leetcode?
# Yes, it works on standard quick sort problems.

# Any problem you faced while coding this:
# Handling edge cases (like already sorted arrays) requires using a good pivot selection strategy.

# Your code here along with comments explaining your approach:
# - Quick Sort is a **divide-and-conquer** algorithm.
# - It selects a **pivot element** and partitions the array such that elements smaller than the pivot go to the left, and elements greater go to the right.
# - We recursively apply the same logic to the left and right partitions until the entire array is sorted.

def partition(arr, low, high):
    """
    This function takes the last element as the pivot, places the pivot at its 
    correct position in the sorted array, and places all smaller elements to 
    the left of the pivot and all greater elements to the right.
    """
    pivot = arr[high]  # Pivot element
    i = low - 1  # Index of the smaller element

    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i += 1  # Increment the index of the smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    # Swap the pivot element with the element at index (i+1)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the partitioning index

def quickSort(arr, low, high):
    """
    The main function that implements Quick Sort.
    """
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)

        # Recursively sort elements before and after the partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i], end=" ")
