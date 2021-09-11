# Python program for implementation of MergeSort
# TC: O(NlogN)
# SC: O(N)
def merge(left,right,arr):
  i = j = k = 0
  nL = len(left)
  nR = len(right)
  # checking for smallest unpicked element from
  # both arrays and over-writing it to original array
  while i < nL and j < nR:
    if left[i] <= right[j]:
      arr[k] = left[i]
      i += 1
    else:
      arr[k] = right[j]
      j += 1
    k += 1
  # At this point, either of left or right sub-array should become empty
  # Now we check for left-over elements from the other array and overwrite the original array
  while i < nL:
    arr[k] = left[i]
    i += 1
    k += 1
  
  while j < nR:
    arr[k] = right[j]
    j += 1
    k += 1



def mergeSort(arr):
  if len(arr) < 2:
    return
  partition = len(arr)//2


  left_arr = arr[:partition]
  right_arr = arr[partition:]

  mergeSort(left_arr)
  mergeSort(right_arr)

  merge(left_arr,right_arr,arr)
  
  
# Code to print the list 
def printList(arr):
  print(*arr, sep = ", ")
    
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
