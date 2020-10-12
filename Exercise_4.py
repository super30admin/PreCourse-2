# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  if len(arr)==1:
    return
  mid=len(arr)//2

  L_h=arr[:mid]
  R_h=arr[mid:]

  mergeSort(L_h)
  mergeSort(R_h)

  i=0
  j=0
  k=0


  while i < len(L_h) and j <len(R_h):
    if L_h[i]<R_h[j]:
      arr[k]=L_h[i]
      i+=1
      
    else:
      arr[k]=R_h[j]
      j+=1
    k+=1


  while i<len(L_h):
    arr[k]=L_h[i]
    i+=1
    k+=1

  while j<len(R_h):
    arr[k]=R_h[j]
    j+=1
    k+=1





# Code to print the list 
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
