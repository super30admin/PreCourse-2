# Python program for implementation of MergeSort


"""

    Student : Shahreen Shahjahan Psyche

    Time Complexity : O(NlogN)
    Memory Complexity : O(logN)

    The code ran successfully

"""
def mergeSort(arr):

    if len(arr) > 1 :

        # Getting the mid point of the array and dividing the array into 2 using the mid point
        mid = len(arr)//2
        L = arr[: mid]
        R = arr[mid :]

        # passing these two arrays to sort or get divided again
        mergeSort(L)
        mergeSort(R)

        # this function merges the two arrays back again
        merge(L, R, arr)

def merge(L, R, arr):

    i = 0
    j = 0
    k = 0

    # checking if the element of the both arrays. The smaller one will get saved everytime.
    while(i<len(L) and j<len(R)):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # When we run out of either of the arrays, we will shift the remaining of the other arrays to the arr
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
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
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
