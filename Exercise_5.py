# Python program for implementation of Quicksort iteratively
# Approach -- In the iterative implementation we 'mimick' the implicit call-stack used in recursive method
# Use a stack separately and managing the sorting. We can use deque.
# append the sub list range indices to stack and pop off top value (l, h index pair) using which we will partition the array
# 1st iteration we consider sub list as the entire list and append (0, - len(arr) - 1) to stack
# Repeat until stack is empty

# Time Complexity -- 
#   Best & Average --> O(N log(N))
#   Worst ---> O(N^2)
# Space Complexity -- O(log(N))
# successfully ran


from collections import deque

# This function is same in both iterative and recursive
def partition(arr, l, h):

  pivotIdx = l
  leftIdx =  l + 1
  rightIdx = h

  while rightIdx >= leftIdx:

    if arr[leftIdx] > arr[pivotIdx] and arr[rightIdx] < arr[pivotIdx]:
      swap(leftIdx, rightIdx, arr)

    if arr[leftIdx] <= arr[pivotIdx]:
      leftIdx += 1

    if arr[rightIdx] >= arr[pivotIdx]:
      rightIdx -= 1

  swap(pivotIdx, rightIdx, arr)
  return rightIdx # pivot element gets sorted at position rightIdx and is the final place
  

def quickSortIterative(arr, l, h):

  # base cases
  if len(arr) == 1:
    return arr
  
  if l >= h:
    return

  stack = deque()
  stack.append((l, h))

# Continue as long as stack is not empty
  while stack:
    startIdx, endIdx = stack.pop()

    pivotIdx = partition(arr, startIdx, endIdx)

    # now add sub list with elements less than pivot to stack
    if pivotIdx - 1 > startIdx:
      stack.append((startIdx, pivotIdx - 1))

    # now add sub list with elements greater than pivot to stack
    if pivotIdx + 1 < endIdx:
      stack.append((pivotIdx + 1, endIdx))

# helper method to swap elements at indices
def swap(i, j, arr):
  arr[i], arr[j] = arr[j], arr[i]


# driver code
arr = [8,5,2,9,5,6,3]
quickSortIterative(arr, 0, len(arr) -1)
# print the sorted list
print(arr)


