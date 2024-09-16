# Python program for implementation of MergeSort
def mergeSort(arr):
    # print(arr)
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    return mergeSortHelper(mergeSort(left), mergeSort(right))


def mergeSortHelper(left, right):
    sortedarr = [None] * (len(left) + len(right))

    k = i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sortedarr[k] = left[i]
            i += 1
        else:
            sortedarr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        sortedarr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        sortedarr[k] = right[j]
        j += 1
        k += 1

    return sortedarr


# write your code here

# Code to print the list
def printList(arr):
    print(arr)


# write your code here

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    arr = mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
