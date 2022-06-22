# Python program for implementation of MergeSort 
# Merge Sort fuction 
# First divide the array into 2 sorted halves
# merge the sorted arrays
  
def mergeSort(arr):
  if len(arr)>1:
    # Dividing the array into 2 sections
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    # Recursively call the mergeSort function
    # On both the arrays
    mergeSort(L)
    mergeSort(R)
    i = j = k = 0
    # Logic to merge two sorted arrays
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        arr[k] = L[i]
        k +=1
        i +=1
      else:
        arr[k] = R[j]
        j += 1
        k += 1
    # Logic for adding the elements in case one of the two
    # arrays have more elements  
    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1
    while j < len(R):
      arr[k] = R[j]
      k += 1
      j += 1
#write your code here
  
# Code to print the list 
def printList(arr): 
  n = len(arr) 
  for i in range(n): 
    print ("%d" %arr[i])
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
