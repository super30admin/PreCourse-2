# Python program for implementation of MergeSort
def mergeSort(arr):
    # write your code here

    if len(arr) > 1:
        mid = len(arr) // 2

        first_half = arr[:mid]
        second_half = arr[mid:]

        mergeSort(first_half)
        mergeSort(second_half)

        merge(arr, first_half, second_half)


def merge(arr, arr1, arr2):
    i = 0
    j = 0
    k = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1



# Code to print the list 
def printList(arr):
    # write your code here
    print(arr)


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
