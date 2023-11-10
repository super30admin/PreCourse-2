# Time Complexity: O(n)
# Space Complexity: O(nlogn)

# Python program for implementation of MergeSort
def mergeSort(arr):
    # write your code here

    if len(arr) > 1:
        mid = len(arr) // 2
        leftArr = arr[:mid]
        rightArr = arr[mid:]
        mergeSort(leftArr)
        mergeSort(rightArr)

        i = 0
        j = 0
        k = 0

        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1
        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1


# Code to print the list
def printList(arr):
    # write your code here

    for i in range(len(arr)):
        print(arr[i])


# driver code to test the above code 
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
