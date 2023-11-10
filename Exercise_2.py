# Python program for implementation of Quicksort Sort

# Time Complexity : O(n)
# Space Complexity : O(1)
# Any problem you faced while coding this : No
# The code finds the element between low and high that is larger than pivot and swaps them
def partition(arr, low, high):
    index = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            index += 1
            arr[index], arr[j] = arr[j], arr[index]
    arr[index+1], arr[high] = arr[high], arr[index+1]
    return (index + 1)


# Time Complexity : O(nlogn)
# Space Complexity : O(logn)
# Any problem you faced while coding this : No
# The code partitions the array from low and high and recursively runs quickSort on them
def quickSort(arr, low, high):
    if len(arr) <= 1:
        return arr
    if low < high:
        partInd = partition(arr, low, high)
        quickSort(arr, low, partInd-1)
        quickSort(arr, partInd+1, high)

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
