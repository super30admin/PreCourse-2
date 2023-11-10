# Time Complexity : Average case O(nlogn), Best case O(n) when elements are already ordered.
# Space Complexity : O(n) since the merge() is not an inplace merge.
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Did not know if there exists an inplace merge algorithm for 2 sorted subarrays.

# Merge sort recursively merges sorted sub arrays to form the final sorted array. 
# The base cases for the sub-arrays are size 0 and size 1
# merge() function is very optimal if the highest element of left subarray is less then lowest element of right subarray.

# Python program for implementation of MergeSort 
def mergeSort(arr):
  mergeSortInner(arr, 0, len(arr)-1)

def mergeSortInner(arr, low, high):
  if high-low < 1:
    return
  mid = low + (high-low)//2
  mergeSortInner(arr, low, mid)
  mergeSortInner(arr, mid+1, high)
  merge(arr, low, mid, high)

def merge(arr, l, mid, h):
  if arr[mid] < arr[mid+1]:
    return
  newarr = []
  l1 = l
  l2 = mid+1
  while l1 <= mid and l2 <= h:
    if arr[l1] < arr[l2]:
      newarr.append(arr[l1])
      l1 += 1
    else:
      newarr.append(arr[l2])
      l2 += 1
  while l1 <= mid:
    newarr.append(arr[l1])
    l1 += 1
  while l2 <= h:
    newarr.append(arr[l2])
    l2 += 1 
  for i in range(l, h+1):    
    arr[i] = newarr[i-l]
  
  
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
