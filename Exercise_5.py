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
    stack = [0] * (h - l + 1)
    top = -1

    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    while top >= 0:

        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        p = partition(arr, l, h)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:", arr)