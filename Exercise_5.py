# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  # choose right most element as pivot
  pivot = arr[h]
  # pointer for greater element 
  i = l - 1
  # loop through array
  for j in range(l, h):
    if arr[j] <= pivot:
      # if the element at j pointer smaller than pivot then swap element i and j position
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  # swap the pivot element with the element at i+1 position
  arr[i+1], arr[h] = arr[h], arr[i+1]
  # return partition position
  return i + 1


def quickSortIterative(arr, l, h):
  #write your code here
  # use stack to store low and high index
  stack = [(l, h)]
  # loop till stack is not empty 
  while stack:
    # pop the low and high from the stack
    low, high = stack.pop()
    if low < high:
      # find the pivot index for the arr with low and high index
      pivotIndex = partition(arr, low, high)
      # push the tuple with the low and pivot index - 1 to stack
      stack.append((low, pivotIndex-1))
      # push the tuple with the pivot index + 1 and high to stack
      stack.append((pivotIndex+1, high))

