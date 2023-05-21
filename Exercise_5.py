# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  pidx = h
  i = l
  for j in range(l, h):
    if arr[j] < arr[pidx]:
      arr[i], arr[j] = arr[j], arr[i]
      i+=1
  arr[i], arr[pidx] = arr[pidx], arr[i]
  return i


def quickSortIterative(arr, l, h):
  if h-l+1 <= 1:
    return
  pivot = partition(arr, l, h)
  stack = [(l, h)]
  while stack:
    (l, h) = stack.pop()
    pivot = partition(arr, l, h)
    if (pivot-1)-l+1 > 1:
      stack.append((l, pivot-1))
    if h-(pivot+1)+1 > 1:
      stack.append((pivot+1, h))



