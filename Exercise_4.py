# Python program for implementation of MergeSort
def mergeSort(arr):
    length=len(arr)
    if length>1:
        mid=length//2

        left=arr[:mid]
        right=arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0

        while (i< len(left)) &(j<len(right)):
            if left[i] <= right[j]:
                arr[k]=left[i]
                i=i+1
            else:
                arr[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            arr[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            arr[k]=right[j]
            j=j+1
            k=k+1


# Code to print the list
def printList(arr):
    print(arr)
    n=[str(i) for i in arr]
    return ",".join(n)


# # driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
