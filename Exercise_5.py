# Time Complexity :  best scenario O(n log n), worst case o(n^2)
# Space Complexity : best scenario O(log n), worst case o(n)
# Did this code successfully run on Leetcode : No 
# Any problem you faced while coding this : No

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

  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return i + 1
  
def quickSortIterative(arr, l, h):
  #write your code here
  size = h - l + 1
  stack = [0] * size

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

    if p - 1 > l:
      top += 1
      stack[top] = 1
      top += 1
      stack[top] = p - 1

    if p + 1 < h:
      top += 1
      stack[top] = p + 1
      top += 1
      stack [top] = h


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSortIterative(arr, 0, n-1)
    print("Sorted array is:")
    for i in range(n):
        print("%d" % arr[i], end=" ")