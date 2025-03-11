# Python program for implementation of MergeSort 

# Time Complexity:
# - Best Case: O(n log n) - Even in the best case, we always divide the array and merge
# - Average Case: O(n log n) - Consistent performance regardless of input data
# - Worst Case: O(n log n) - Performance remains stable even with worst-case inputs

# Space Complexity:
# - O(n) - We need auxiliary space for storing temporary subarrays during merging

def mergeSort(arr):
  if len(arr) > 1:
    # Finding the mid of the array
    mid = len(arr) // 2
    
    # Dividing the array elements into 2 halves
    L = arr[:mid]
    R = arr[mid:]
    
    # Sorting the first half
    mergeSort(L)
    
    # Sorting the second half
    mergeSort(R)
    
    i = j = k = 0
    
    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # Checking if any element was left
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
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
