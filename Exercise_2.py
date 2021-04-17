# Python program for implementation of Quicksort Sort 
import collections


# give you explanation for the approach
def partition(nums, lower, upper):
    pivot = nums[upper]

    i = lower

    for j in range(lower, upper):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[upper] = nums[upper], nums[i]

    return i

    # write your code here


# Function to do Quick sort
def quicksort(nums, lower, upper):
    if lower < upper:
        pivot = partition(nums, lower, upper)
        quicksort(nums, lower, pivot - 1)
        quicksort(nums, pivot + 1, upper)
    else:
        return

    # write your code here


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),


