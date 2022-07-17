# Python program for implementation of MergeSort  

"""   
Time complexity:  O(nlogn)
Space Complexity: O(n)

Explanation: 

Split the array in half 
all merge sort on each half sort them recursively 
merge both sorted halves into one sorted array 

"""
def mergeSort(arr):
    if len(arr) > 1:
      
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
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
    arr = [12, 11, 13, 5, 6, 7,1,2,3,4,4,44,3,2,2,5,7,5,3,2,2,2]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
