#Time Complexity: O(n logn)
#Space Complexity: O(n) --Temporary arrays during merge

# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle point
        L = arr[:mid]        # Divide the array elements into 2 halves
        R = arr[mid:]

        mergeSort(L)         # Sort the first half
        mergeSort(R)         # Sort the second half

        # Merging process
        i = j = k = 0

        # Copy data to temp arrays L[] and R[] into arr[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Check if any elements are left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

  
  #write your code here
  
# Code to print the list 
def printList(arr):
  for i in arr:
        print(i, end=" ")
  print() 

    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
