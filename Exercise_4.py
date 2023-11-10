# // Time Complexity : O(NlogN)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode :
# // Any problem you faced while coding this : No


# // Your code here along with comments explaining your approach
"""
1. calculate mid index of the array , and call mergesort with left and right halves recursively untill length of array is 1
2. As single element is sorted , it will start comparing left side and right side array , merge them
3. Need to merge residual elements from left or right array
"""


# Python program for implementation of MergeSort
def mergeSort(arr):
    # write your code here
    if len(arr) == 1:
        return
    mid = len(arr) // 2
    leftSub = arr[:mid]
    rightSub = arr[mid:]
    mergeSort(leftSub)
    mergeSort(rightSub)

    i = j = k = 0

    while i < len(leftSub) and j < len(rightSub):
        if leftSub[i] < rightSub[j]:
            arr[k] = leftSub[i]
            i += 1
        else:
            arr[k] = rightSub[j]
            j += 1
        k += 1

    while i < len(leftSub):
        arr[k] = leftSub[i]
        i += 1
        k += 1

    while j < len(rightSub):
        arr[k] = rightSub[j]
        j += 1
        k += 1


# Code to print the list
def printList(arr):
    print("Elements in an array {}".format(arr))
    # write your code here


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr) 
