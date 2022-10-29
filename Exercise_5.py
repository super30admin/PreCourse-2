# Time Complexity: O(N^2) worst case for already sorted, O(NlogN) average
# Space Complexity: O(N) worst case, O(logN) average

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr,low,high):
  pivot = arr[high]
  i = low - 1

  for j in range(low,high):
      if arr[j] <= pivot:
          i += 1
          arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return (i+1)

def quickSortIterative(arr, low, high):
  #write your code here
  length = high - low + 1
  stack = [0]*length

  top = 0
  stack[top] = low
  top += 1
  stack[top] = high

  while top >= 0:

    high = stack[top]
    top -= 1
    low = stack[top]
    top -= 1

    pivot = partition(arr,low,high)

    if pivot-1 > low:
      top += 1
      stack[top] = low
      top += 1
      stack[top] = pivot - 1

    if pivot+1 < high:
      top += 1
      stack[top] = pivot + 1
      top += 1
      stack[top] = high