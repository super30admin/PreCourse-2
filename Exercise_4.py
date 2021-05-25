# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr) == 1:
        return

    mid = round(len(arr) / 2)
    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)

    i = 0
    j = 0

    # aux_arr = []
    k = 0

    while i <=len(left)-1 and j <=len(right)-1:
        if left[i]<=right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k+=1

    while i<=len(left)-1:
        arr[k] = left[i]
        i = i + 1
        k += 1

    while j<=len(right)-1:
        arr[k] = right[j]
        j = j + 1
        k += 1
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 

#T(n) = n(logn)
#S(n) = O(n)