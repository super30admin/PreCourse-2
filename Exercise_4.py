# Python program for implementation of MergeSort 
def mergeSort(arr):
  arr_len = len(arr)

  if arr_len == 1:
    return arr

  mid = arr_len // 2
  left = mergeSort(arr[:mid])
  right = mergeSort(arr[mid:])
  i, j, k = 0, 0, 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      arr[k] = left[i]
      i += 1
    else:
      arr[k] = right[j]
      j += 1
    k += 1
  
  while i < len(left):
    arr[k] = left[i]
    i += 1
    k += 1
  
  while j < len(right):
    arr[k] = right[j]
    j += 1
    k += 1
  
  return arr

# Code to print the list 
def printList(arr): 
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is: \n")
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: \n") 
    printList(arr) 
