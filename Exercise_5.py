# Time Complexity : O[n]
# Space Complexity : O[n/2] ~ O[n]
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
  pivot_index = low
  pivot = arr[pivot_index]

  while low < high:
    while low < len(arr) and arr[low] <= pivot:
        low+=1
    while arr[high] > pivot:
        high-=1
    if low < high:
        arr[low], arr[high] = arr[high], arr[low]
    
  arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
  return high


def quickSortIterative(arr, l, h):
  stack = []
  stack.append(l)
  stack.append(h)

  while len(stack) > 0:
    h = stack.pop(len(stack)-1)
    l = stack.pop(len(stack)-1)

    p = partition(arr, l, h)

    if p-1 > l:      
      stack.append(l)
      stack.append(p - 1)
    
    if p+1 < h:
      stack.append(p + 1)
      stack.append(h)
