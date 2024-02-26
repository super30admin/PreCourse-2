# Python program for implementation of Quicksort Sort


# Time complexity = O(nlogn) space complexity = O(n)
# give you explanation for the approach
def partition(arr, low, high):
    i, j = low, high
    pivot = arr[low]

    while i < j:

        while arr[i] <= pivot and (
            i < high
        ):  # loop while we get left element greater than pivot
            i += 1

        while arr[j] > pivot and (
            j >= low
        ):  # loop while we get right element smalle than pivot
            j -= 1
        if i < j:
            (arr[i], arr[j]) = (arr[j], arr[i])  # swap arr[i] and arr[j]
    (arr[low], arr[j]) = (arr[j], arr[low])  # swap pivot element with position j
    return j


# Function to do Quick sort
def quickSort(arr, low, high):

    # write your code here
    if low < high:
        j = partition(
            arr, low, high
        )  # partition the list while we get list of single element
        quickSort(arr, low, j)  # sort left part
        quickSort(arr, j + 1, high)  # sort right part


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
