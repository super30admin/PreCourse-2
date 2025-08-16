# Python program for implementation of Quicksort
#Time Complexity: O(n log n) worst case O(N2)
#Space Complexity: O(n log n)
# This function is same in both iterative and recursive

"""QuickSort is a divide-and-conquer sorting algorithm where we usually Choose a pivot element from the array.
Partition the array:

All elements smaller than the pivot go to the left.

All elements greater than the pivot go to the right.

Ieratively apply the same steps to the left and right subarrays.
"""
def partition(arr, l, h):

#write your code here
 
  pivot = arr[h]
  i = l - 1

  for j in range(l, h):
      if arr[j] < pivot:
          i += 1
          swap(arr, i, j)

  swap(arr, i + 1, h)
  return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]  


def quickSortIterative(arr, l, h):
  #write your code here

  # Create an explicit stack for storing subarray bounds
    stack = []

    # Push initial range onto stack
    stack.append((l, h))

    # Process stack until empty
    while stack:
        # Pop top subarray bounds
      l, h = stack.pop()

      if l < h:
          # Partition the array
          partition = partition(arr, l, h)

          # Push left subarray bounds if it has more than 1 element
          if partition - 1 > l:
              stack.append((l, partition - 1))

          # Push right subarray bounds if it has more than 1 element
          if partition + 1 < h:
              stack.append((partition + 1, h))

