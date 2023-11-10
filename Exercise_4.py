# Python program for implementation of MergeSort 
def mergeSort(arr):
      if len(arr) > 1:
            r = len(arr)//2
            L = arr[:r]
            M = arr[r:]

            mergeSort(L)
            mergeSort(M)

            i = j = k = 0
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