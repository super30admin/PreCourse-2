# Python program for implementation of Quicksort
import random


def partition(arr, l, h):
  #write your code here
  pivot_idx = random.randint(l, h)
  
  pivot = arr[pivot_idx]
  
  arr[pivot_idx], arr[h] = arr[h], arr[pivot_idx]  # Move pivot to end

  i = l - 1 # smallest element index
  
  # traverse all elements in subarray
  for j in range(l, h):
      # if current element is smaller than or equal to pivot
      if arr[j] <= pivot:
          i += 1
          arr[i], arr[j] = arr[j], arr[i]  # swap elements at i and j
          
  arr[i + 1], arr[h] = arr[h], arr[i + 1]  # swap pivot to its correct position
  return i + 1  # return the index of pivot after partitioning


def quickSortIterative(arr, l, h):
  #write your code here
  
  stack = []
  stack.append((l, h))  # push initial indices onto the stack
  
  while stack:
    
    low, high = stack.pop()
    if low<high:
      pivot_idx = partition(arr, low, high)
      
      stack.append((low, pivot_idx-1))
      stack.append((pivot_idx+1, high))
    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
    

