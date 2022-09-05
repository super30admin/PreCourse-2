# Time Complexity: O(nlogn)
# Space Complexity: O(n)

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  tmp = (l - 1)
  p = arr[h]

  for i in range(l, h):
    if arr[i] <= p:
      tmp += 1

      arr[i], arr[tmp] = arr[tmp], arr[i]

  arr[tmp+1], arr[h] = arr[h], arr[tmp+1]

  return (tmp+1)


def quickSortIterative(arr, l, h):
  #write your code here
  s = h - l + 1
  stack = [0] * s

  top = 0

  stack[top] = l
  top += 1
  stack[top] = h
  
  while top >= 0:
    h = stack[top]
    top -= 1
    l = stack[top]
    top -= 1

    p = partition(arr, l, h)

    if p-1 > l:
      top = top + 1
      stack[top] = l
      top = top + 1
      stack[top] = p - 1

    if p+1 < h:
      top = top + 1
      stack[top] = p + 1
      top = top + 1
      stack[top] = h

arr = [5, 10, 16, 3, 7, 1]
quickSortIterative(arr, 0, len(arr)-1)
print('Sorted Array: ', arr)