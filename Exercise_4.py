"""
Leetcode - NA
TC - O(NlogN) - binary partition with O(N) each, SC - O(N)
Challenge - Merging two sorted list into original array
"""

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)

        # merge two sorted arrays
        # TC - O(N), N = length of original arr, SC - O(N)
        i, j, k = 0, 0, 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            elif R[j] <= L[i]:
                arr[k] = R[j]
                j += 1
            k += 1

        # add remaining to the original list
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list
def printList(arr):
    print(arr)
    # write your code here


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

'''
[1, 3, 5] [2, 4, 6]

'''
