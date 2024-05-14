'''
Time: O(nlogn)
Space: O(logn) on average since that much stack memory is consumed for recusive calls at a time
'''

# Python program for implementation of Quicksort Sort

# # # give you explanation for the approach
'''
1. Select a random pivot value within the array.
2. Partition the array such that all values less than the pivot value fall in the left partition and
  and all the values greater than the pivot value fall in the right partition.
3. Place the pivot value in between the 2 partitions.
4. Repeat all the steps on the left and right partition recursively.
5. The final result is a sorted array.
'''

import random

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

# Function to do Quick sort 
def quickSort(arr, low, high): 
  if low >= high:
    return

  pivotIndex = random.randint(low, high)  # select a random pivot index to improve worst case time complexity
  newPivotPosition = partition(arr, low, high, pivotIndex) # partition the array arround the pivot index such that all lesser values are on left and bigger values are on right
  quickSort(arr, low, newPivotPosition-1) # recurse on the left partition
  quickSort(arr, newPivotPosition+1, high) # recurse on the right partition

# Driver code to test above 
arr = [10, 17, -8, 9, 1, 5, 2, 4, -3, 7, 32, -28, 20, 0]
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted arr is:") 
for i in range(n): 
  print (arr[i], end = ' ')
