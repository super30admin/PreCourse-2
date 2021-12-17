# Python program for implementation of MergeSort 
def mergeSort(arr):

  if len(arr) == 1:
    print(arr)
    return arr

  left = 0
  right = len(arr) - 1
  middle = left + (right - left) // 2

  leftSort = mergeSort(arr[left:middle + 1])
  rightSort = mergeSort(arr[middle + 1:right + 1]) 

  p = 0
  q = 0
  currSorted = []
  while p < len(leftSort) and q < len(rightSort):
    if leftSort[p] <= rightSort[q]:
      currSorted.append(leftSort[p])
      p += 1
    else:
      currSorted.append(rightSort[q])
      q += 1
  while p < len(leftSort):
    currSorted.append(leftSort[p])
    p += 1
  while q < len(rightSort):
    currSorted.append(rightSort[q])
    q += 1
  
  print(currSorted)
  return currSorted

  #write your code here
  
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
