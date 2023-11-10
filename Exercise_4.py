# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Python program for implementation of MergeSort 

def merge(left,right,arr):
  i, j, k = 0, 0, 0
  while(i<len(left) and j<len(right)):
    if left[i]<=right[j]:
      arr[k] = left[i]
      i += 1
      k += 1
    else:
      arr[k] = right[j]
      j += 1
      k += 1
  while(i<len(left)):
    arr[k] = left[i]
    i += 1
    k += 1
  while(j<len(right)):
    arr[k] = right[j]
    j += 1
    k += 1

def mergeSort(arr):
  
  #write your code here
  n = len(arr)
  if n == 1:
    return
  mid = n//2
  left = arr[:mid]
  right = arr[mid:]
  mergeSort(left)
  mergeSort(right)
  merge(left,right,arr)
  
# Code to print the list 
def printList(arr): 
  for e in arr:
    print(e,end=" ")
  print("\n")
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
