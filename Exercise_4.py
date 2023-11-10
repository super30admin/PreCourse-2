# Python program for implementation of MergeSort 
def merge(arr, low, mid, high):
  i = low
  j = mid+1
  temp = [0 for i in range(high+1)]
  k = low
  while(i<=mid and j<=high):
    if arr[i]<=arr[j]:
      temp[k] = arr[i]
      i = i+1
      k = k+1   
    else:
      temp[k] = arr[j]
      j = j+1
      k = k+1
  while(i<=mid):
    temp[k] = arr[i]
    i = i+1
    k = k+1

  while(j<=high):
    temp[k] = arr[j]
    j = j+1
    k = k+1
  
  for i in range(low, high+1):
    arr[i] = temp[i]

def mergeSort(arr, low, high):
  if low < high:
    mid = (low+high)//2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    merge(arr, low, mid, high)


  
  #write your code here
  
# Code to print the list 
def printList(arr): 
    print(arr)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr, 0 , len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
