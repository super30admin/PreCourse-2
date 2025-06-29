'''
IterativeQuickSort
'''

# Time Complexity : # O(n log n) on average, O(n^2) in the worst case when the pivot is always the smallest or largest element.
# Space Complexity : # O(log n) for the stack space used in the iterative approach, as we are using an auxiliary stack to store indices.
# Did this code successfully run on Leetcode : Yes, the code runs successfully on my local environment and passes test case.
# Any problem you faced while coding this : Yes, understanding how to implement the iterative version of quicksort was a bit challenging, especially managing the stack for indices and ensuring that the partitioning logic was correctly applied without recursion.

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  i = (l - 1) # index of smaller element
  pivot = arr[h] # pivot element

  for j in range(l, h):
    # If current element is smaller than or equal to pivot
    if arr[j] <= pivot:
      i = i + 1
      arr[i], arr[j] = arr[j], arr[i] # swap
  
  arr[i + 1], arr[h] = arr[h], arr[i + 1] # swap pivot element with the element at i + 1
  return i + 1 # return the index of the pivot element


def quickSortIterative(arr, l, h):
  #write your code here
  # Create an auxiliary stack
  stack = [0] * (h - l + 1) # stack to store the indices
  top = -1 # Initialize top of stack
  top += 1 # Push initial values of l and h to stack
  stack[top] = l
  top += 1
  stack[top] = h
  while top >= 0:
    # Pop h and l
    h = stack[top]
    top -= 1
    l = stack[top]
    top -= 1

    # Set pivot element at its correct position
    p = partition(arr, l, h)

    # If there are elements on the left side of the pivot, push them to stack
    if p - 1 > l:
      top += 1
      stack[top] = l
      top += 1
      stack[top] = p - 1

    # If there are elements on the right side of the pivot, push them to stack
    if p + 1 < h:
      top += 1
      stack[top] = p + 1
      top += 1
      stack[top] = h
  return arr

# Driver code to test above
if __name__ == "__main__":
  arr = [10, 7, 8, 9, 1, 5]
  n = len(arr)
  print("Unsorted array:", arr)
  quickSortIterative(arr, 0, n - 1)
  print("Sorted array:", arr)
  # Output: Sorted array: [1, 5, 7, 8, 9, 10]

