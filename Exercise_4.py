# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
    current_size = 1
    while current_size < len(arr) - 1:
        left = 0
        while left < len(arr) - 1:
            mid = min((left + current_size - 1), (len(arr) - 1))
            right = ((2 * current_size + left - 1, len(arr) - 1)[2 * current_size + left - 1 > len(arr) - 1])

            merge(arr, left, mid, right)
            left = left + current_size * 2
        current_size = 2 * current_size
        
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = arr[left + i]
    for j in range(0, n2):
        R[j] = arr[mid + j + 1]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] > R[j]:
            arr[k] = R[j]
            j += 1
        else:
            arr[k] = L[i]
            i += 1
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
    
    #write your code here
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    
    arr = [12, 11, 13, 5, 6, 7]  
    print("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is:", end=" ")  
    printList(arr)
