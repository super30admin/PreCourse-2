# Python program for implementation of MergeSort 
def mergeSortedArray(arr1, arr2):
    i= 0
    j= 0
    merged_array = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
    #print("Merged: ", merged_array)
    return merged_array


def mergeSort(arr):
    #write your code here
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    
    left = arr[:mid]
    #print("Split ", left)
    right = arr[mid:]
    #print("Split ", right)
    
    left = mergeSort(left)
    right = mergeSort(right)
    
    return mergeSortedArray(left, right)
  
# Code to print the list 
def printList(arr): 
    #write your code here
    print(" ".join(map(str,arr)))
      
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
