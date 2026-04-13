# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[h]
    i = l - 1

    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quickSortIterative(arr, l, h):
  # Create an explicit stack
  stack = []

  # push initial range
  stack.append((l, h))

  # Process stack until empty
  while stack:
      l, h = stack.pop()

      # Partition the array
      pi = partition(arr, l, h)

      # If elements on left side of pivot, push left side
      if pi - 1 > l:
          stack.append((l, pi - 1))

      # If elements on right side of pivot, push right side
      if pi + 1 < h:
          stack.append((pi + 1, h))

