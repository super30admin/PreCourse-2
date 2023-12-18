#Time complexity: Average case - O(n log n), Worst case - O(n^2)
#Space Complexity: Best case - O(log n), Worst case - O(n)

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l - 1

  for j in range(l, h):
    if arr[j] <= pivot:
      i = i + 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return i + 1


def quickSortIterative(arr, l, h):
  #write your code here
  stack = [0] * (h - l + 1)
  top = -1

  top = top + 1
  stack[top] = l
  top = top + 1
  stack[top] = h

  while top>= 0:
    h = stack[top]
    top = top - 1
    l = stack[top]
    top = top - 1

    pivot_index = partition(arr, l, h)

    if pivot_index - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = pivot_index - 1

    if pivot_index + 1 < h:
            top = top + 1
            stack[top] = pivot_index + 1
            top = top + 1
            stack[top] = h


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),