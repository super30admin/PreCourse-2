"""
Exercise_4 : Merge Sort.
Time Complexity : O(nlogn)
    
Space Complexity : O(N)
As all elements are copied into an auxiliary array 
so N auxiliary space is required for merge sort. 

@name: Rahul Govindkumar_RN27JUL2022
"""
# Python program for implementation of MergeSort 

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted 
    
def mergeSort(arr, l, r):
  
  #write your code here
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l+r)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)  
  
  
# Code to print the list 
def printList(arr): 
    
    
    #write your code here
    for i in range(len(arr)):
        print(arr[i], end=" ")
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr, 0, len(arr)-1) 
    print("\nSorted array is: ", end="\n") 
    printList(arr) 
