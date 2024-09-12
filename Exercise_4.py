# Python program for implementation of MergeSort 
# Time complexity - O(N log (N))
# Space Complexity - O(n log (N))
# Successfully ran

def mergeSort(arr):
  if len(arr) == 1:
    return arr
  
  middleIdx = len(arr) // 2
  leftArr = arr[:middleIdx]
  rightArr = arr[middleIdx:]

  # apply recursion on both sub arrays
  mergeSort(leftArr)
  mergeSort(rightArr)
  
  leftIdx = rightIdx = resultIdx = 0

  while leftIdx < len(leftArr) and rightIdx < len(rightArr):
    if leftArr[leftIdx] < rightArr[rightIdx]:
      arr[resultIdx] = leftArr[leftIdx]
      leftIdx += 1

    else:
      arr[resultIdx] = rightArr[rightIdx]
      rightIdx += 1

    resultIdx += 1

  # if any one sub array runs out of numbers check the remaining sub array
  while leftIdx < len(leftArr):
    arr[resultIdx] = leftArr[leftIdx]
    leftIdx += 1
    resultIdx += 1

  while rightIdx < len(rightArr):
    arr[resultIdx] = rightArr[rightIdx]
    rightIdx += 1
    resultIdx += 1

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
