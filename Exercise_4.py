# Time Complexity : O(n*log(n))
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : N.A.
# Any problem you faced while coding this : Had a little trouble because I'm new to Python.

# Your code here along with comments explaining your approach
# Python program for implementation of MergeSort
def merge(arr, left, right):
    del arr[:]
    idxL = 0
    idxR = 0
    while idxL < len(left) and idxR < len(right):
        if left[idxL] <= right[idxR]:
            arr.append(left[idxL])
            idxL += 1
        else:
            arr.append(right[idxR])
            idxR += 1

    arr.extend(left[idxL:])
    arr.extend(right[idxR:])
    return arr

# implemented mergeSort using the divide and conquer strategy, broke down the whole array into len(arr)
# arrays each with length one and for the merge method compared each values and recreated the sorted array.
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) / 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)
        merge(arr, left, right)

    return arr


# Code to print the list 
def printList(arr):
    print(arr)

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [100, 9, 11, 4, 8, 0, 1, 100]
    print ("Given array is")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ")
    printList(arr)
