# Python program for implementation of MergeSort
'''
Runs in O(nlog(n))
'''
def merge(arr, left, right, mid):
    temp = [None] * (right - left + 1)
    i = left
    j = mid + 1
    k = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for t in range(left, right + 1):
        arr[t] = temp[t - left]


def sort(arr, l, r):
    if l >= r:
        return
    m = l + (r - l) // 2
    sort(arr, l, m)
    sort(arr, m+1, r)
    merge(arr, l, r, m)


def mergeSort(arr):
    #write your code here
    sort(arr, 0, len(arr) - 1)


# Code to print the list
def printList(arr):
    #write your code here
    print(arr)


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
