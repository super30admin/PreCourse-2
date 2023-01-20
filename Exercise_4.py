# Python program for implementation of MergeSort

# Time Complexity - O(nlogn) - We divide the array each iteration hence O(logn) and we
# merge the 2 arrays back again hence O(n).
# Space complexity - O(n) - Stack space as we perform recursive calls.

# Dividing the array into halves to get left and right array. Doing this until
# left and right array have 1 element each. Merging the left and right array after sorting.
def mergeSort(arr):

    if len(arr) == 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    mergeLists(left, right, arr)

# We compare the left and right array elements one by one, whichever
# is smaller is added to the original array.
def mergeLists(left,right, arr):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i<len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j<len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


# Code to print the list
# Time complexity - O(n)
# Space complexity - O(1)
def printList(arr):
    print(arr)


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
