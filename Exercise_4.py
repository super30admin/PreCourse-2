# Python program for implementation of MergeSort 

# Time Complexity : O(nlogn)
# Space Complexity : O(1)

def merge(arr1, arr2,arr):


    n1 = len(arr1)
    n2 = len(arr2)

    i = 0
    j = 0
    k = 0

    while( i<n1 and j<n2):
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            k += 1
            i += 1
        else:
            arr[k] = arr2[j]
            k += 1
            j += 1

    while i<n1:
        arr[k] = arr1[i]
        k += 1
        i += 1
    while j<n2:
        arr[k] = arr2[j]
        k += 1
        j += 1

    return arr

def mergeSort(arr): 
    n = len(arr) 

    if n <=1:
        return arr
    else:
        mid = n//2
        left = arr[:mid]

        arr1 = mergeSort(left)

        right = arr[mid:]
        arr2 = mergeSort(right)
        arr = merge(arr1,arr2,arr)
        return arr
  #write your code here
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
