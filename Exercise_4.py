# Python program for implementation of MergeSort
# Time complexity o(nlogn) n size of array
# space complexity o(n)

def merge(arr, l, mid, h):
    L = arr[l:mid+1]
    R = arr[mid+1: h+1]
    k, i, j = l, 0, 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        k += 1
        i += 1
    while j < len(R):
        arr[k] = R[j]
        k += 1
        j += 1
    return arr


def mergeSortImplement(arr, l, h):
    if h-l+1 <= 1:
        return arr
    mid = (l+h)//2
    mergeSortImplement(arr, l, mid)
    mergeSortImplement(arr, mid+1, h)
    merge(arr, l, mid, h)
    return arr


def mergeSort(arr):
    l, h = 0, len(arr)-1
    arr = mergeSortImplement(arr, l, h)
    return arr


# Code to print the list
def printList(arr):
    for n in arr:
        print(n)


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
