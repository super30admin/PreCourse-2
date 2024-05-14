'''
Time: O(nlogn)
Space:  O(n) since a buffer array is created in the merge function
        the maximim size of this buffer array will be n (during the final merge)
        Although a buffer array is created in every recursive call, the memory is deallocated after the call completes,
        since Python has automatic garbage collection.
        Thus at a given time the algorithm takes at the most n exta memory
        Thus overall space complexity is O(n)
'''

# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr) <= 1:
    return
  recursiveMergeSort(arr, 0, len(arr)-1)

def recursiveMergeSort(arr, left, right):
  if left >= right:
    return
  midIdx = (left + right)//2
  recursiveMergeSort(arr, left, midIdx)
  recursiveMergeSort(arr, midIdx + 1, right)
  merge(arr, left, midIdx, midIdx+1, right)

def merge(arr, left1, left2, right1, right2):
  bufferArray = []
  leftIdx = left1
  rightIdx = right1
  while leftIdx <= left2 and rightIdx <= right2:
    if arr[leftIdx] <= arr[rightIdx]:
      bufferArray.append(arr[leftIdx])
      leftIdx += 1
    else:
      bufferArray.append(arr[rightIdx])
      rightIdx += 1
    
  while leftIdx <= left2:
    bufferArray.append(arr[leftIdx])
    leftIdx += 1

  while rightIdx <= right2:
    bufferArray.append(arr[rightIdx])
    rightIdx += 1

  mainIdx = left1
  for item in bufferArray:
    arr[mainIdx] = item
    mainIdx += 1

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
