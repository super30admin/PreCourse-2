# Author : Akaash Trivedi
# Time Complexity : O(n log n)
# Space Complexity : O(n) - copying arr in left and right sub arrays
# Did this code successfully run on Leetcode : Leetcode #912
# Any problem you faced while coding this : No

# Python program for implementation of MergeSort 
def mergeSort(arr):
  n = len(arr)
  if n < 2:
    return
  mid = n//2
  left = arr[:mid]
  right = arr[mid:]

  mergeSort(left)
  mergeSort(right)
  merge(left,right,arr)

def merge(l,r,arr):
  nl = len(l)
  nr = len(r)
  i = j = k = 0
  while i < nl and j<nr:
      if l[i] <= r[j]:
         arr[k] = l[i]
         i += 1
      else:
         arr[k] = r[j]
         j += 1
      k +=1
  while i<nl:
    arr[k] = l[i]
    i +=1
    k +=1
  while j<nr:
    arr[k]=r[j]
    j+=1
    k+=1

# Code to print the list 
def printList(arr): 
  for i in range(len(arr)):
    print(arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
