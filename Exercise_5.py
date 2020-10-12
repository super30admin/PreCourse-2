# Python program for implementation of Quicksort
# Problem faced while solving: can't think of an Iterative way.

# This function is same in both iterative and recursive
def partition(arr,low,high):

  # write your code here

  pivot = arr[high]
  i = low - 1

  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      # Swap
      arr[j], arr[i] = arr[i], arr[j]

  # Get i+1th position for the pivot
  arr[i+1], arr[high] = arr[high], arr[i+1]                  
  return i+1


def quickSortIterative(arr, l, h):
  # write your code here
  if not arr: return
  if len(arr) == 1: return arr

  if l < h:
  
    pos = partition(arr, l, h)
    quickSortIterative(arr, l, pos - 1)
    quickSortIterative(arr, pos + 1, h)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1)

print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
