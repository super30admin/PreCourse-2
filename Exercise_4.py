#//Time Complexity : O(nlogn)
#// Space Complexity : O(n)
#// Did this code successfully run on Leetcode : Yes
#// Any problem you faced while coding this : No
# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
    if len(arr) <= 1:
        return arr
    
    #diving into two parts
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    
    #Recurrsive call for split until will get 1 one element
    mergeSort(L)
    mergeSort(R)
    
    #Merging 
    i = j = k = 0
    
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
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
    
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for a in arr:
        print(a)    
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
