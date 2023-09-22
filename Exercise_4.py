# Python program for implementation of MergeSort 
def mergeSort(arr):

    if len(arr) > 1:
        partition = (len(arr)) //2
        arrA = arr[:partition]
        arrB = arr[partition:]
        mergeSort(arrA)
        mergeSort(arrB)
        i, j ,k = 0, 0, 0
        while (i < len(arrA)) and (j < len(arrB)):
            if arrA[i] < arrB[j]:
                arr[k] = arrA[i]
                i += 1
            else:
                arr[k] = arrB[j]
                j += 1
            k += 1
        while i < len(arrA):
            arr[k] = arrA[i]
            i += 1
            k += 1
        while j < len(arrB):
            arr[k] = arrB[j]
            j += 1
            k += 1

# Code to print the list 
def printList(arr): 
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr)
    print("Sorted array is: ", end="\n") 
    printList(arr)
