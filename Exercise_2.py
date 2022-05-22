# Python program for implementation of Quicksort Sort 

# give you explanation for the approach
# Time complexity:O(nlogn)
# Space Complexity: O(1)
# Did you face any difficulty: Yes (with recursion concepts)
def partition(arr, low, high):
    # write your code here
    while low < high:
        pivot = arr[high]
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
    return high

# Function to do Quick sort
def quickSort(arr, low, high):
    # write your code here
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot+1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
