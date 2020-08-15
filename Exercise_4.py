# Python program for implementation of MergeSort 

#Time Compleixty: O(nlogn)
def merge(arr, first, second):
  i, j, k = 0, 0, 0

  while i < len(first) and j < len(second):
    if first[i] < second[j]:
      arr[k] = first[i]
      i += 1
      
    else:
      arr[k] = second[j]
      j += 1
    k += 1
  
  while i < len(first):
    arr[k] = first[i]
    k += 1
    i += 1

  while j < len(second):
      arr[k] = second[j]
      k += 1
      j += 1

def mergeSort(arr):
  low = 0
  high = len(arr) - 1
  if low < high:
    mid = (len(arr)) // 2
    first = arr[:mid]
    second = arr[mid:]
    mergeSort(first)
    mergeSort(second)
    merge(arr, first, second)

  
  #write your code here
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    print (arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end = " ")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end = " ") 
    printList(arr) 