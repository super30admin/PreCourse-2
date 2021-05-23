# Python program for implementation of Quicksort Sort
# Time Complexity : O(nLogn)
#  Space Complexity : O(logn)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : Calculating compexities

# give you explanation for the approach
def partition(low, high, arr):
    pivot_index = (low+high)//2
    pivot = arr[pivot_index]

    while low < high:
        # increment low till it gets element greater than  pivot
        while low < len(arr) and arr[low] <= pivot:
            low += 1

        #decrement low till it gets element lower than  pivot
        while arr[high] > pivot:
            high -= 1

        # If start and high have not crossed each other,swap the numbers on start and high
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]

    #swap
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]

    # Returning high pointer to divide the array into 2
    return high


# Function to do Quick sort 
def quickSort(arr, low, high):
    if low < high:
        # p is partitioning index
        p = partition(low, high, arr)

        # Sort elements before partition and after partition
        quickSort(arr,low, p - 1)
        quickSort(arr,p + 1, high)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
