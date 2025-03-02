# Python program for implementation of Quicksort Sort


# give you explanation for the approach
# Divide-and-conquer sorting algorithm that recursively partitions the array using a pivot and sorts the sub-arrays

# Time complexity:
# 1) best/aveg case: O(nlog n) because partitioning at all the levels due to recursion
# 2) worst case: O(n^2) when pivot is either smallest or the largest element

# space complexity:
# 1) best case: O(log n): recursion stack size
# 2) worst case: O(n) : when recursion stack goes as deep as n


def partition(arr, low, high):
    # write your code here
    pivot = arr[low]  # choosing pivot as the first element of an array
    i = low  # Moves from left to right, looking for elements greater than pivot
    j = high  # Moves from right to left. looking for elements smaller than pivot

    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1  # incrementing i untill current element is less than or equals to pivot
        while arr[j] > pivot and j >= low + 1:
            j -= 1  # decrementing j untill current element is greater than pivot
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]  # swap elements at i and j
    arr[low], arr[j] = (
        arr[j],
        arr[low],
    )  # swap pivot with j that makes pivot at the right place and all the elements on the right side will be greater than j and left side smaller
    return j  # Return the pivot index


# Function to do Quick sort
def quickSort(arr, low, high):

    # write your code here
    if low < high:
        p_index = partition(arr, low, high)  # get the pivot index
        quickSort(arr, low, p_index - 1)  # left side of the arrray
        quickSort(arr, p_index + 1, high)  # right side array


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
