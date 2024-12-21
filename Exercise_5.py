# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
# T: O(n^2), S: O(n)
def partition(arr, l, h):
  # Choose the last element as pivot
  pivot = arr[h]  
  i = l - 1

  for j in range(l, h):
      if arr[j] <= pivot:
          i += 1
          arr[i], arr[j] = arr[j], arr[i]  # Swap

    # Place the pivot in the correct position
  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return i + 1


def quickSortIterative(arr):
  # Base Case
  if len(arr) <= 1:
        return arr

  # Stack to simulate recursion
  stack = [(0, len(arr) - 1)]

  while stack:
      start, end = stack.pop()
      if start < end:
          # Partition the array
          pivot_index = partition(arr, start, end)

            # Push subarray indices onto the stack
          stack.append((start, pivot_index - 1))  # Left subarray
          stack.append((pivot_index + 1, end))  # Right subarray

  return arr

# Driver Code:
arr = [38, 27, 43, 3, 9, 82, 10]
quickSortIterative(arr)
print("Sorted array:", arr)