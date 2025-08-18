# Python program for implementation of Quicksort

# Time Complexity :O(n*log(n))
# Space Complexity :O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
# Your code here along with comments explaining your approach: The code implements iterative QuickSort using an explicit stack instead of recursion. The partition function rearranges elements around a pivot (last element), placing smaller elements to the left and larger ones to the right, and returns the pivot’s final index. The quickSortIterative function pushes subarray bounds onto the stack, processes them in a loop, and sorts the array by repeatedly partitioning until the entire array is sorted.


# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  i = l - 1
  x = arr[h]

  for j in range(l, h):
    if arr[j] <= x:
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

  while top >= 0:
    h = stack[top]
    top = top -1
    l = stack[top]
    top = top - 1

    p = partition(arr, l, h)

    if p -1 > l:
      top = top + 1
      stack[top] = l
      top = top + 1
      stack[top] = p - 1

    if p + 1 < h:
      top = top + 1
      stack[top] = p + 1
      top = top + 1
      stack[top] = h
     
arr = [4, 3, 5, 2, 1, 3, 2, 3]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i])
