# Python program for implementation of MergeSort 
def mergeSort(arr):    
  #write your code here
  if len(arr) <= 1:
    return
  mid = (len(arr))//2
  larr = arr[:mid]
  rarr = arr[mid:]
  mergeSort(larr)
  mergeSort(rarr)
  i, j = 0, 0
  k = 0
  while i < len(larr) and j < len(rarr):
    if larr[i] <= rarr[j]:
       arr[k] = larr[i]
       i += 1
    else:
       arr[k] = rarr[j]
       j += 1
    k += 1

  while i < len(larr):
    arr[k] = larr[i]
    i += 1
    k += 1
  
  while j < len(rarr):
    arr[k] = rarr[j]
    j += 1
    k += 1

# Code to print the list 
def printList(arr): 
    
    #write your code here
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
