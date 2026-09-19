# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l - 1

  for j in range(l, h):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  i += 1
  arr[i], arr[h] = arr[h], arr[i]
  return i


def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  stack.append(l)
  stack.append(h)

  while stack:

    high = stack.pop()
    low = stack.pop()

    pivotIndex = partition(arr, low, high)

    # Left side
    if low < pivotIndex-1:
      stack.append(low)
      stack.append(pivotIndex-1)

    # Right side
    if pivotIndex + 1 < high:
      stack.append(pivotIndex+1)
      stack.append(high)

arr = [10, 7, 8, 9, 1, 5]

quickSortIterative(arr, 0, len(arr)-1)
print("Sorted array is:")
for i in range(len(arr)):
    print(arr[i])

