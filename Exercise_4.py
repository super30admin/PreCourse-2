# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  if len(arr) > 1:
     
    r = len(arr) // 2
    L = arr[ : r]
    M = arr[r : ]

    mergeSort(L)
    mergeSort(M)

    i = 0
    j = 0
    k = 0

    while i < len(L) and j < len(M):
        
      if L[i] < M[j]:
        arr[k] = L[i]
        i += 1
      else:
        arr[k] = M[j]
        j += 1

      k += 1
    
    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1

    while j < len(M):
      arr[k] = M[j]
      j += 1
      k += 1

  return arr
    
      
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in arr:
      print(i)

  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
