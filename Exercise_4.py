# Python program for implementation of MergeSort 

# Time Complexity : O(nlogN)
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : maximum recursion depth exceeded error, had to fix print function
# Find Mid Point of a Singly Linked List.

def mergeSort(arr):
  if len(arr) > 1:
    #write your code here
    mid = len(arr) // 2
    #left and right array, recursively then merge
    L = arr[:mid]
    R = arr[mid:]

    mergeSort(L)
    mergeSort(R)

    i =0; j =0 ; k = 0

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
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
