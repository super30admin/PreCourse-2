# Python program for implementation of MergeSort
def mergeSort(arr):
  helper(arr, 0, len(arr) - 1)

def helper(arr, start, end):
    # Base Case
    if start >= end:
        return
    # Find mid
    mid = start + (end - start) // 2

    # Recursive Case - Sort
    helper(arr, start, mid)
    helper(arr, mid + 1, end)

    # Merge
    i = start
    j = mid + 1
    aux = []
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            aux.append(arr[i])
            i += 1
        else:
            aux.append(arr[j])
            j += 1
    # Collect leftover elements
    while i <= mid:
        aux.append(arr[i])
        i += 1
    while j <= end:
        aux.append(arr[j])
        j += 1
    arr[start:end+1] = aux[:]
    return

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
