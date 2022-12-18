# Python program for implementation of MergeSort 
#time: O(nlog(n))
def mergeSort(arr,l,r):

    if l < r:

	    # Same as (l+r)//2, but avoids overflow for
	    # large l and h
	    m = l+(r-l)//2

	    # Sort first and second halves
	    mergeSort(arr, l, m)
	    mergeSort(arr, m+1, r)
	    merge(arr, l, m, r)


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0    
    j = 0
    k = l
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
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
    mergeSort(arr,0,len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
