# Python program for implementation of MergeSort

def merge(arr, arr1, arr2):
  i = 0
  j = 0
  k = 0
  while(i<len(arr1) and j<len(arr2)):
    if(arr1[i]<arr2[j]):
      arr[k] = arr1[i]
      i+=1
    else:
      arr[k] = arr2[j]
      j+=1
    k+=1
  while(i<len(arr1)):
    arr[k] = arr1[i]
    k+=1
    i+=1
  while(j<len(arr2)):
    arr[k] = arr2[j]
    k+=1
    j+=1

def mergeSort(arr):
  if(len(arr) == 1):
    return
  mid = len(arr)//2
  arr_left = arr[:mid]
  arr_right = arr[mid:]
  mergeSort(arr_left)
  mergeSort(arr_right)
  merge(arr,arr_left, arr_right)
  
# Code to print the list 
def printList(arr):
  print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 