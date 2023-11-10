"""
Time Complexity : O( n*log(n) )
Space Complexity : O(n)
Did this code successfully run on Leetcode : N/A
Any problem you faced while coding this : No
"""


# Python program for implementation of MergeSort
def mergeSort(arr):
    '''
    first divide the array into sub arrays by dividing it from middle until single element is left.Then
    merge those divided array and sorting its element them.
    '''
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    # return arr


# Code to print the list
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