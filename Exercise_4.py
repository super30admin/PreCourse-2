# Time Complexity : O(nlog(n))
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Couldn't find the problem in LeetCode
# Any problem you faced while coding this : No

# Python program for implementation of MergeSort 

def merge(arr, left, mid, right):
  i = left
  j = mid + 1
  res = []
  # Merge 2 sorted halves of array in a new array - res
  while i <= mid and j <= right:
    if arr[i] < arr[j]:
      res.append(arr[i])
      i += 1
    else:
      res.append(arr[j])
      j += 1
  while i <= mid:
    res.append(arr[i])
    i += 1
  while j <= right:
    res.append(arr[j])
    j += 1
  # Copy the contents of the merged sorted array res to original array
  k = 0
  for i in range(left, right+1):
    arr[i] = res[k]
    k += 1


def mergeSortHelper(arr, left, right):
  if left >= right:
    return
  mid = (left + right) // 2
  # Sort left half of the array
  mergeSortHelper(arr, left, mid)
  # Sort right half of the array
  mergeSortHelper(arr, mid+1, right)
  # Merge the two sorted halves of the array
  merge(arr, left, mid, right)


def mergeSort(arr):
  
  #write your code here
  n = len(arr)
  mergeSortHelper(arr, 0, n-1)
  
# Code to print the list 
def printList(arr): 
    
  #write your code here
  print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
