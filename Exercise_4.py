# Python program for implementation of MergeSort 
def mergeSort(arr, l, h):
  
  #write your code here
  if l < h:
    mid = (l+h)//2
    mergeSort(arr, l, mid)
    mergeSort(arr, mid+1, h)
    merge(arr, l, mid, h)
  
# Code to print the list 
def printList(arr): 
  for i in arr:
    print(i)
    
    #write your code here

def merge(arr, l, m, h):
  i = l
  j = m+1
  temp = [0 for i in range(h+1)]
  k = l
  while(i<=m and j<=h):
    if arr[i]<=arr[j]:
      temp[k] = arr[i]
      i = i+1
      k = k+1   
    else:
      temp[k] = arr[j]
      j = j+1
      k = k+1
  while(i<=m):
    temp[k] = arr[i]
    i = i+1
    k = k+1

  while(j<=h):
    temp[k] = arr[j]
    j = j+1
    k = k+1

  for i in range(l, h+1):
    arr[i] = temp[i]
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr, 0, len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 