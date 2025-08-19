# Python program for implementation of Quicksort Sort 

# The average time complexity is O(nlogn), however, if the pivot value that we chose is not very optimal then the time complexity becomes O(n^2)
# We basically chose a pivot point usually the end value in the arr, have two pointers left and i which iterates, if at any given point the value at position i
# is less than the pivot value we swap with arr[left]. Finally, once all the swapping is complete, we swap the pivot with arr[left] and then the pivot value will be in sorted position
# Do the same for left and right partition
def quickSort(arr, low, high):
    if (high - low + 1 <= 1):
        return arr
    pivot = arr[high]
    left = low

    for i in range(low, high):
        if arr[i] < pivot:
            temp = arr[left]
            arr[left] = arr[i]
            arr[i] = temp
            left += 1
    #Switch the pivot and arr[left] in the end
    arr[high] = arr[left]
    arr[left] = pivot

    quickSort(arr, left + 1, high)
    quickSort(arr, low, left -1)

    return arr


# write your code here

# Driver code to test above 
arr = [5, 10, 9, 3, 1, 0]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
