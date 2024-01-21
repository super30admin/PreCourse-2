# Time Complexity : O(nLogn) where n is the size of the array
# Space Complexity : Need to discuss. It depends on the recursion call stack
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Python program for implementation of MergeSort


# two sorted arrays: from l to mid and mid + 1 to r
def mergeSortedArrays(arr, l, r, mid):
    # replacing the index at k with the smaller value as we iterate
    k = l
    # aux space for the sorted arrays
    arr1 = []
    arr2 = []

    for i in range(l, mid + 1):
        arr1.append(arr[i])
    for j in range(mid + 1, r + 1):
        arr2.append(arr[j])

    arr1CurrentIndex = 0
    arr2CurrentIndex = 0
    # two pointers starting from the beginning of each sorted array
    while arr1CurrentIndex < len(arr1) and arr2CurrentIndex < len(arr2):
        if arr1[arr1CurrentIndex] <= arr2[arr2CurrentIndex]:
            arr[k] = arr1[arr1CurrentIndex]
            arr1CurrentIndex += 1
        else:
            arr[k] = arr2[arr2CurrentIndex]
            arr2CurrentIndex += 1
        k += 1

    # remaining elements
    while arr1CurrentIndex < len(arr1):
        arr[k] = arr1[arr1CurrentIndex]
        arr1CurrentIndex += 1
        k += 1

    while arr2CurrentIndex < len(arr2):
        arr[k] = arr2[arr2CurrentIndex]
        arr2CurrentIndex += 1
        k += 1

    return


def mergeSort(arr, l, r):
    # write your code here
    # only one element
    if r <= l:
        return
    mid = int((l + r) / 2)
    mergeSort(arr, l, mid)
    mergeSort(arr, mid + 1, r)
    mergeSortedArrays(arr, l, r, mid)


# Code to print the list
def printList(arr):
    # write your code here
    for el in arr:
        print(el)


# driver code to test the above code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr, 0, len(arr) - 1)
    print("Sorted array is: ", end="\n")
    printList(arr)
