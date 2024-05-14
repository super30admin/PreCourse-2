'''
Time: O(nlogn)
Space: O(logn) on average since that much stack memory is consumed at a time
'''

# Python program for implementation of Quicksort

import random
# This function is same in both iterative and recursive
def swap(arr, a, b):
  arr[a], arr[b] = arr[b], arr[a]

def partition(arr, low, high, pivotIndex):
  pivot = arr[pivotIndex]
  swap(arr, low, pivotIndex)
  partitionMarker = low+1
  for traverser in range(low+1, high+1):
    if arr[traverser] < pivot:
      swap(arr, partitionMarker, traverser)
      partitionMarker += 1
  swap(arr, low, partitionMarker-1)
  return partitionMarker-1

def quickSortIterative(arr, l, h):
  boundsStack = [(l, h)]

  while len(boundsStack) > 0:
    # print('Stack status: ', boundsStack)
    low, high = boundsStack.pop()
    pivotIndex = random.randint(low, high)
    newPivotPosition = partition(arr, low, high, pivotIndex)

    if low < newPivotPosition-1:
      boundsStack.append((low, newPivotPosition-1))

    if newPivotPosition+1 < high:
      boundsStack.append((newPivotPosition+1, high))

# Driver code to test above 
arr = [10, 17, -8, 9, 1, 5, 2, 4, -3, 7, 32, -28, 20, 0]
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted arr is:") 
for i in range(n): 
  print (arr[i], end = ' ')
