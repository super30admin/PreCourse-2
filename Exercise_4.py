# Python program for implementation of MergeSort
def merge(arr,low,high,mid):
    left_array = arr[low:mid+1]
    right_array = arr[mid+1:high + 1]
    i,j = 0,0
    k = low

    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

    while i < len (left_array):
        arr[k] = left_array[i]
        i += 1
        k += 1
    while j < len(right_array):
        arr[k] = right_array[j]
        j += 1
        k += 1
    return arr


def mergeSort(arr,low,high):
    if low < high:
        mid = (low + high) //2
        mergeSort(arr,low,mid)
        mergeSort(arr, mid + 1, high)
        merge(arr,low, high, mid)


def printList(arr):
    for i in arr:
        print(i, end=" ")

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr,0,len(arr)-1)
    print("\nSorted array is: ", end="\n")
    printList(arr)
