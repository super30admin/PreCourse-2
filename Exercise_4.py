# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr) <= 1:
    return

  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]

  mergeSort(left)
  mergeSort(right)

  leftIndex = rightIndex = combinedIndex = 0
  while leftIndex < len(left) and rightIndex < len(right):
    if left[leftIndex] <= right[rightIndex]:
      arr[combinedIndex] = left[leftIndex]
      leftIndex += 1
    else:
      arr[combinedIndex] = right[rightIndex]
      rightIndex += 1

    combinedIndex += 1

    arr[combinedIndex:] = left[leftIndex:] + right[rightIndex:]
  
# Code to print the list 
def printList(arr): 
  print(*arr)    
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
