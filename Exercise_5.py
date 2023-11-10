"""
TC:O(logn)
SC:O(n)

"""
def partition(arr, l, h):
  #write your code here
  i = (l - 1)
  pivot = arr[h]
  for j in range(l, h):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return (i + 1)


def quickSortIterative(arr, l, h):
  #write your code here
  size = h - l + 1
  stack = [0] * (size)
  top = -1
  top = top + 1
  stack[top] = l
  top = top + 1
  stack[top] = h
  while top >= 0:
    h = stack[top]
    top = top - 1
    l = stack[top]
    top = top - 1
    p = partition( arr, l, h )
    if p-1 > l:
      top = top + 1
      stack[top] = l
      top = top + 1
      stack[top] = p - 1
    if p + 1 < h:
      top = top + 1
      stack[top] = p + 1
      top = top + 1
      stack[top] = h
# Driver Code
if __name__ == '__main__' :
    arr = [4, 2, 6, 9, 2]
    n = len(arr)
    # Calling quickSort function
    quickSortIterative(arr, 0, n - 1)
    for i in range(n):
        print(arr[i], end = " ")

