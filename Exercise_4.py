# Python program for implementation of MergeSort 
# Time Complexity : O(n log n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Online GDB executed.
# Any problem you faced while coding this : No.

def mergeSort(arr):
 # Base case: if the list has one or no element, it's already sorted.
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle index
        L = arr[:mid]        # Dividing the array elements into 2 halves
        R = arr[mid:]
        
        # Sort the first half
        mergeSort(L)
        # Sort the second half
        mergeSort(R)
        
        i = j = k = 0
        
        # Merge the sorted halves into arr
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # Check if any element was left in L
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        # Check if any element was left in R
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def printList(arr): 
    for i in arr:
        print(i, end=" ")
    print()  

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
