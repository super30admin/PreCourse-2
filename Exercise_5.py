# Time Complexity: Not able to calculate
# Space Complexity: Not able to calculate
# Did this code successfully run on Leetcode: No
# Any problem you faced while coding this: Didn't understand the logic of the problem

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  i = (l - 1)
  pivot = arr[h]
  for j in range(l,h):
    if arr[j] <= pivot:
      i+=1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[h] = arr[h], arr[i+1]
  return i + 1



def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  stack.append((l,h))
  while stack:
    l,h = stack.pop()
    if l < h:
      p = partition(arr, l, h)
      if p-1 > l:
        stack.append((l, p - 1))
      if p+1 < h:
        stack.append((p + 1, h))

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
print(arr)