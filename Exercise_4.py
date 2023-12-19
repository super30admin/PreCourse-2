## Time Complexity : O(N2)
## Space Complexity : O(N)
## Did this code successfully run on Leetcode : Yes
## Any problem you faced while coding this : No
##
##
## Your code here along with comments explaining your approach

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)

    return merge(left_half, right_half)


def printList(arr):
    for element in arr:
        print(element, end=" ")
    print()


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
