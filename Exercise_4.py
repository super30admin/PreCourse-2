# Time Complexity: O(nlogn)
# Space Complexity: O(n)
# Python program for implementation of MergeSort 
from turtle import right


def mergeSort(arr):
  if len(arr)>1:
    mid = len(arr)//2
    leftarr = arr[:mid]
    rightarr = arr[mid:]
    mergeSort(leftarr)
    mergeSort(rightarr)
    i = 0
    j = 0
    k = 0
    while i < len(leftarr) and j < len(rightarr):
      if rightarr[j] < leftarr[i] :
        arr[k] = rightarr[j]
        j += 1
      else:
        arr[k] = leftarr[i]
        i += 1
      k += 1
    
    while i < len(leftarr):
      arr[k] = leftarr[i]
      k += 1
      i += 1
    
    while j < len(rightarr):
      arr[k] = rightarr[j]
      k += 1
      j += 1
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):
      print(arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
