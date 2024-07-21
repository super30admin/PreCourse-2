# Python program for implementation of Quicksort
# Time Complexity : O(n^2)
# Space Complexity : O(n) stack
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# This function is same in both iterative and recursive


def partition(arr,low,high):
  i, j = low, high
  pivot = low
  # print(arr[pivot])
  while i < j:
    while i < j and arr[i] < arr[pivot]:
      i += 1
    while i < j and arr[j] > arr[pivot]:
      j -= 1
      if i < j:
        arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[pivot] = arr[pivot], arr[j]

  return j


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
    part = partition(arr, l, h)

    if part - 1 >= l:
      top += 1
      stack[top] = l
      top += 1
      stack[top] = part - 1
    
    if part + 1 < h:
      top += 1
      stack[top] = part + 1
      top += 1
      stack[top] = h
    


arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 