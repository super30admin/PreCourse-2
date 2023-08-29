# Time Complexity : O(nlogn) 
#  Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No  

# Python program for implementation of MergeSort 
def mergeSort(arr):
  mergeSortInternal(arr, 0, len(arr)-1)
  
  #write your code here
def mergeSortInternal(arr, low, high):
  if low >= high:
    return
  mid = (low + high) // 2
  mergeSortInternal(arr, low, mid)
  mergeSortInternal(arr, mid +1 , high)
  merge(arr, low, mid, mid+1, high)
  
def merge(arr, l1, u1, l2, u2):
  new = []
  i = l1
  j = l2
  while i <= u1 and j <= u2:
    if arr[i] <= arr[j]:
      new.append(arr[i])
      i+= 1
    else:
      new.append(arr[j])
      j+=1
  while i <= u1: 
    new.append(arr[i])
    i += 1
  while j <= u2:
    new.append(arr[j])
    j += 1
  k = 0
  for i in range(l1, u2 +1):
    arr[i] = new[k]
    k += 1



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
