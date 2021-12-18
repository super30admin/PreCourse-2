# Python program for implementation of MergeSort
def mergeSort(arr):
    # check if the array has more than one element
    if len(arr) > 1:
        central_index = int(len(arr) / 2)

        # splitting and copying data in temporary arrays
        L = arr[:central_index]
        R = arr[central_index:]

        # applying merge sort to spilt recursievely
        mergeSort(L)
        mergeSort(R)

        # for merge
        i = j = k = 0

        #comparing and replacing
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i = i + 1
            else:
                arr[k] = R[j]
                j = j + 1
            k = k + 1

        # we will also check, if there are any unchecked elements from both L and R arrays
        while i < len(L):
            arr[k] = L[i]
            i = i + 1
            k = k + 1

        while j < len(R):
            arr[k] = R[j]
            j = j + 1
            k = k + 1

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
