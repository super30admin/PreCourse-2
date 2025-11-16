# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1  # Index of the smaller element
  for j in range(low, high):
    # If current element is smaller than or equal to pivot
    if arr[j] <= pivot:
      i = i + 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1


def quickSortIterative(arr, l, h):
  # Sorts an array using iterative Quick Sort by managing a stack of sub-array boundaries to be processed.
  if not arr:
    return
  # Create a stack to store low and high indices
  # We use a list and append/pop from the end for stack behavior
  stack = []
  # Push initial low and high indices
  stack.append(l)
  stack.append(h)

  # Keep popping from stack while it is not empty
  while stack:
    high = stack.pop()
    low = stack.pop()
    # Get pivot element's position after partitioning
    p = partition(arr, low, high)
    # If there are elements on the left side of pivot, push them to stack
    if p - 1 > low:
      stack.append(low)
      stack.append(p - 1)
      # If there are elements on the right side of pivot, push them to stack
      if p + 1 < high:
        stack.append(p + 1)
        stack.append(high)

  return arr

# driver code to test the above code 
arr = [10, 80, 30, 90, 40, 50, 70]
print(f"Original array: {arr}")
sortedArr = quickSortIterative(arr, 0, len(arr)-1)
print(f"Sorted array:  {sortedArr}")