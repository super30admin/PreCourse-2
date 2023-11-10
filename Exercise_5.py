# Time Complexity : O(nlogn) for best and average, O(n^2) for worst
# Space Complexity : O(logn)
# Did this code successfully run on Leetcode : Yes on VSCODE
# Any problem you faced while coding this : No
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]

  i = l - 1

  for j in range(l, h):
      if arr[j] <= pivot:
          i = i + 1
          (arr[i], arr[j]) = (arr[j], arr[i])

  (arr[i + 1], arr[h]) = (arr[h], arr[i + 1])
  return i + 1

def quickSortIterative(arr, l, h):
  #write your code here
  #  auxiliary stack
    size = h - l + 1
    stack = [0] * (size)
 
    top = -1
 
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
 
    # Keep popping from stack while is not empty
    while top >= 0:
 
        # Pop high and low
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
 
        # sorted array
        p = partition( arr, l, h )

        # push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        #  push right side to stack
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is: ", arr) 
