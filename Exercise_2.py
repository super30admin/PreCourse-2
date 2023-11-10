# Time Complexity : O(n^2) worst case O(n log n)
# Space Complexity : O(log n)
# Did this code successfully run on Leetcode : Couldn't find on Leetcode
# Any problem you faced while coding this : None
# Python program for implementation of Quicksort Sort

# give you explanation for the approach
'''
We take the last element of the array as pivot, which we will use as the basis for all comparisons
Then we iterate through the list arrange items with respect to the pivot
This sequence have the pivot element in the correct position
Now take the last element from the two new list around the pivot and sort those list accordingly
i finds all value greater than pivot and j finds all value smaller than pivot
'''


def partition(arr, low, high):
    i = low
    j = high - 1
    pivot = arr[high]

    while i < j:
        while i < high and arr[i] < pivot:
            i += 1
        while j > low and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[high] = arr[high], arr[i]
    return i


# write your code here


# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quickSort(arr, low, pivot_index - 1)
        quickSort(arr, pivot_index + 1, high)


# write your code here

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
