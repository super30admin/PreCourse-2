# Time Complexity : O(nlogn) Average case, O(n^2) worst case 
#  Space Complexity : O(n) not sure 
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Yes but not bigger problems
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
from collections import deque
def partition(arr, low, high):
  #write your code here
  j = low + 1
  for i in range(low+1, high+1): 
      if arr[i] < arr[low]:
          arr[j], arr[i] = arr[i], arr[j] 
          j +=1 
  arr[low], arr[j-1] =  arr[j-1], arr[low]
  return j-1

def quickSortIterative(arr, l, h):
  #write your code here
  stack = deque()
  stack.append(l)
  stack.append(h)
  while stack:
    h, l= stack.pop(), stack.pop()
    pivot = partition(arr, l, h)
    if abs(l - (pivot - 1)) > 1:
      stack.append(l)
      stack.append(pivot-1)
    if abs(h - (pivot+1)) > 1:
      stack.append(pivot+1)
      stack.append(h)

arr = [10, 7, 8, 9, 1, 5] 
print(arr)
quickSortIterative(arr, 0, len(arr)-1)
print(arr)