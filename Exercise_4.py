# Python program for implementation of MergeSort
"""
    time complexity: O(nlog(n))
    space complexity: O(n)
"""


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        arr_left = arr[:mid]
        arr_right = arr[mid:]
        mergeSort(arr_left)
        mergeSort(arr_right)

        i = j = k = 0
        while i < len(arr_left) and j < len(arr_right):
            if arr_left[i] < arr_right[j]:
                arr[k] = arr_left[i]
                i += 1
            else:
                arr[k] = arr_right[j]
                j += 1
            k += 1
        while i < len(arr_left):
            arr[k] = arr_left[i]
            i += 1
            k += 1
        while j < len(arr_right):
            arr[k] = arr_right[j]
            j += 1
            k += 1


# Code to print the list 
def printList(arr):
    for x in arr:
        print(x, end=' ')
    print()


# driver code to test the above code 
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
