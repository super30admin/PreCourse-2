# Time Complexity : O(nlogn)
# Space Complexity : O(logn) for the maximum size of the stack at any point in time
# Did this code successfully run on Leetcode : Yes, but TLEd on large array consisting of just one number duplicated everywhere.
# Any problem you faced while coding this : -

# The quickSort function is called iteratively on various splits of the array.
# We use a stack to maintain the bounds of the various sub-arrays resulting from each partition() call

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



