# Python program for implementation of Quicksort

# Time Complexity: O(n log n)

# Space Complexity: O(log n)

# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot = arr[h]  # Take the last element as pivot
  i = l - 1 # Index of smaller element

  for j in range(l, h):
      if arr[j] <= pivot:
        i += 1
        arr[i], arr[j] = arr[j], arr[i]  # Swap if element <= pivot
  arr[i + 1], arr[h] = arr[h], arr[i + 1]  # Move pivot to correct position
  return i + 1


def quickSortIterative(arr, l, h):
    size = h - l + 1 # Create an auxiliary stack
    stack = [0] * size

    top = -1 # Initialize top of stack

    top += 1 # Push initial values of l and h to stack
    stack[top] = l
    top += 1
    stack[top] = h

    while top >= 0: # Keep popping from stack while it's not empty
        h = stack[top] # Pop h and l
        top -= 1
        l = stack[top]
        top -= 1

        p = partition(arr, l, h) # Set pivot element at its correct position

        if p - 1 > l: # If there are elements on the left side of pivot, push them to stack
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1

        if p + 1 < h: # If there are elements on the right side of pivot, push them to stack
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h

if __name__ == "__main__":
    arr = [6, 1, 8, 9, 2, 5, 4]
    n = len(arr)
    quickSortIterative(arr, 0, n - 1)
    print("Sorted array is:")
    print(arr)

