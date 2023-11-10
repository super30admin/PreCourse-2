# Python program for implementation of MergeSort 
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
def mergeSort(arr):
  if len(arr) < 2:
    return
  
  l = 0
  r = len(arr)
  m = (l + r)//2

  leftArr = []
  rightArr = []

  i = 0
  j = m
  while i < m:
    leftArr.append(arr[i])
    i += 1
  while j < r:
    rightArr.append(arr[j])
    j += 1

  mergeSort(leftArr)
  mergeSort(rightArr)
  merge(arr, leftArr, rightArr)
  
def merge(arr, leftArr, rightArr):
  nL = len(leftArr)
  nR = len(rightArr)
  i = j = k = 0

  while i < nL and j < nR:
    if leftArr[i] < rightArr[j]:
      arr[k] = leftArr[i]
      i += 1
    else:
      arr[k] = rightArr[j]
      j += 1
    k += 1
  
  while i < nL:
    arr[k] = leftArr[i]
    i += 1
    k += 1

  while j < nR:
    arr[k] = rightArr[j]
    j += 1
    k += 1
  
# Code to print the list 
def printList(arr): 
  for x in arr:            #can also use print function directly on list
    print(x, end = " ")
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr)
