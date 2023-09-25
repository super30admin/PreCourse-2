# Python program for implementation of Quicksort Sort

# Time Complexity : O(n^2)
# Space Complexity : O(n) based on number of recursion calls made by the function, where n = # of elements
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : yes
# 1. I forgot to add a condition where low < len(arr)-1 while moving low ptr, index out of range
# 2. I realized later that before swapping I got to check low<high condition again even though its in while loop with the same condition
# 3. Did not know quick sort earlier, learnt on the go
# 4. Unsure of space complexity

# swap function - traditional way
def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

# give you explanation for the approach


def partition(arr, low, high):
    # pivot index is set at the start (idx = o)
    pivot_idx = low
    pivot = arr[pivot_idx]

    # continue with the while loop until low does not cross high ptr
    while low < high:
        # Check if element referenced by low ptr is <= pivot. If yes, keep going.
        while arr[low] <= pivot and low < len(arr)-1:
            low += 1
        # check if element referenced by high ptr is > pivot. If yes, keep going
        while arr[high] > pivot:
            high -= 1

        # At any point whenever the above two loops exit, swap elements referenced by low & high ptr
        if low < high:
            swap(low, high, arr)

    # swap high ptr element with pivot whenever low crosses high
    swap(pivot_idx, high, arr)
    return high


# write your code here
# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # find partition idx
        partition_idx = partition(arr, low, high)
        # sort left partition recursively
        quickSort(arr, low, partition_idx-1)
        # sort right partition recursively
        quickSort(arr, partition_idx + 1, high)


# write your code here

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i], end=" "),
