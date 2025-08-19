# Python program for implementation of MergeSort
# Time Complexity is O(nlogn) as it uses divide and conquer logic to split the arr into equal halves.
# Space Complexity is O(n)
def merge(arr, s, mid, e):
    L = arr[s: mid+1]
    R = arr[mid+1: e+1]

    i = 0
    j = 0
    k = s

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
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, s, e):
    if (e - s + 1 <= 1):
        return arr

    mid = (s + e) // 2

    mergeSort(arr, s, mid)
    mergeSort(arr, mid+1, e)

    merge(arr, s, mid, e)

    return arr
  
  #write your code here
  
# Code to print the list 
def printList(arr): 
    print(arr)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr, 0, len(arr)-1)
    print("Sorted array is: ", end="\n") 
    printList(arr) 
