# Time Complexity : O(NlogN)
# Space Complexity : O(1)

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  i = (l - 1)        
  p = arr[h]     
  
  for j in range(l, h): 
    if arr[j] <= p: 
      i += 1
      arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i + 1], arr[h] = arr[h], arr[i + 1] 
    return (i + 1) 

def quickSortIterative(arr, l, h):
  #write your code here
  if l < h: 
    pi = partition(arr, l, h) 
    quickSortIterative(arr, l, pi-1) 
    quickSortIterative(arr, pi + 1, h) 
