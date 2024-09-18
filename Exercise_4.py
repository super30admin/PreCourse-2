# Python program for implementation of MergeSort
def mergeSort(arr):
    # if arr consists of just two elements, no need to merge them
    if len(arr) < 2:
        return
    # calculating the mid point  for the array
    mid = len(arr) // 2
    # calculating left and right subarrays
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # calling mergeSort on left and right subarrays
    mergeSort(left_arr)
    mergeSort(right_arr)

    # finally merging the two sorted arrays together to produce the final result
    merge(arr, left_arr, right_arr)


def merge(arr, left_arr, right_arr):
    i = 0
    j = 0
    k = 0

    # comparing the elements two split arrays and adding them into the resultant array in order
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end="")
    print()


# driver code to test the above code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)


# time complexity is O(log n) for dividing and O(n) for merging
# space complexity is O(n) for mergesort and O(logn) for recursion
