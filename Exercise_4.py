# Time Complexity : O(N log(N))
# Space Complexity : O(N log (N))

# Exercise 4 : Merge Sort
# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2
    
    #cutting array into 2 halves
    L = arr[:mid]
    R = arr[mid:]

    #sorting both halves
    mergeSort(L)
    mergeSort(R)

    i = j = k = 0
    #Copying data to temporary arrays
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
