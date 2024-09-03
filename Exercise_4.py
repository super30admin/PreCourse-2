# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left_arr = arr[0:mid]
    
    left_merged = mergeSort(left_arr)
    
    right_arr = arr[mid:len(arr)]
    right_merged = mergeSort(right_arr)
    merged = merge(left_merged, right_merged)
    return merged

def merge(arr1, arr2):
    merged = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    if i<len(arr1):
      merged += arr1[i:]
    if j<len(arr2):
      merged += arr2[j:]
    return merged
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):
        print(arr[i], end=" ")
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr)
    sorted_array =  mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(sorted_array) 
   