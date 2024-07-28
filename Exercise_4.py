# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)
        
        i = j = k = 0
        l = len(left)
        r = len(right)
        
        while i < l and j < r:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < l:
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < r:
            arr[k] = right[j]
            j += 1
            k += 1

    
  
  #write your code here
  
# Code to print the list 
def printList(arr): 
    print(arr,end=" ")
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
