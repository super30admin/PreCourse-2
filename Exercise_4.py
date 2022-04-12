# Python program for implementation of MergeSort 
# Time Complexity : O(Nlog(N))
# Space Complexity : O(N)

def mergeSort(arr):
  sortedArr = mergeSortHelper(arr)
  # copy back
  arr.clear()
  arr.extend(sortedArr)


def mergeSortHelper(arr):
  if len(arr) == 1: return arr

  mid = len(arr) // 2
  left_part = mergeSortHelper(arr[:mid])
  right_part = mergeSortHelper(arr[mid:])

  return merge(left_part, right_part)


def merge(left, right):
  result = []
  i = j = 0

  while i<len(left) and j<len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  
  while i<len(left):
    result.append(left[i])
    i += 1
  while j<len(right):
    result.append(right[j])
    j += 1
  
  return result

  
# Code to print the list 
def printList(arr): 
    print(arr)
    #write your code here

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
