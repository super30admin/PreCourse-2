# Time Complexity: O(n log n)

# Space Complexity: O(n)

# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  if len(arr) > 1:
        mid = len(arr) // 2 # Find the middle point to divide the array into two halves
        L = arr[:mid]   # Left half
        R = arr[mid:]   # Right half
        
        mergeSort(L) # Sort the first and second halves
        mergeSort(R)
        
        i = j = k = 0 # Merge the sorted halves

        while i < len(L) and j < len(R): # Copy data to temp arrays L[] and R[]
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L): # Check if any element was left in L
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R): # Check if any element was left in R
            arr[k] = R[j]
            j += 1
            k += 1
  
# Code to print the list 
def printList(arr): 
    
    for i in arr:
        print(i, end=" ")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is: ", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
