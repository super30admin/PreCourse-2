# Python program for implementation of MergeSort 

def merge(left,right,arr):
  nl = len(left)
  nr = len(right)
  i,j,k = 0,0,0

  while(i<nl and j<nr):
    if left[i]<=right[j]:
      arr[k]=left[i]
      i+=1
    else:
      arr[k]=right[j]
      j+=1
    k+=1

  while(i<nl):
    arr[k]=left[i]
    k+=1
    i+=1
  
  while(j<nr):
    arr[k]=right[j]
    k+=1
    j+=1

def mergeSort(arr):
  
  #write your code here
  n = len(arr)
  if n==1:
    return

  mid = n//2
  left = arr[0:mid]
  right = arr[mid:]

  mergeSort(left)
  mergeSort(right)
  merge(left,right,arr)

  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in arr:
      print(i,end=" ")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
