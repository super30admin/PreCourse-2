def merge(array, left, mid, right):
  # Array is sorted from left to mid
  leftSortedArray = arr[left:mid+1]
  # Array is sorted from mid+1 to right
  rightSortedArray = arr[mid+1:right+1]
  # Start of writerindex
  writerIdx = left
  leftIdx = 0
  rightIdx = 0

  while leftIdx < len(leftSortedArray) and rightIdx < len(rightSortedArray):
    if leftSortedArray[leftIdx] < rightSortedArray[rightIdx]:
      arr[writerIdx] = leftSortedArray[leftIdx]
      leftIdx+=1
    else:
      arr[writerIdx] = rightSortedArray[rightIdx]
      rightIdx+=1
    writerIdx+=1
  
  while leftIdx < len(leftSortedArray):
    arr[writerIdx] = leftSortedArray[leftIdx]
    leftIdx+=1
    writerIdx+=1

  while rightIdx < len(rightSortedArray):
    arr[writerIdx] = rightSortedArray[rightIdx]
    rightIdx+=1
    writerIdx+=1

def mergeSortRecursive(arr, left, right):
  # We have to sort the array from left to right
  if left >= right:
      return
  # we take the mid
  mid = (left + right) // 2
  # Sort the left hafl
  mergeSortRecursive(arr, left, mid)
  # Sort the right half
  mergeSortRecursive(arr, mid+1, right)
  # Merge the 2 sorted halves
  merge(arr, left, mid, right)

# Python program for implementation of MergeSort 
def mergeSort(arr):
  mergeSortRecursive(arr, 0, len(arr)-1)
  
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
