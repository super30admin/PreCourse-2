# Time Complexity : Best - Ω(nlog(n)), Average - θ(nlog(n)), Worst - O(n^2)
# Space Complexity : Worst space complexity - O(n), Average and Best space complexity - O(log(n))
# Did this code successfully run on Leetcode : Couldn't find the problem in LeetCode
# Any problem you faced while coding this : No

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  # Let the last element in the subarary be the pivotelement
  pivotelement = arr[h]
  pivotindex = l
  # Move all elements in the subarray which are less than or equal to the pivotelement to the starting of the array
  for i in range(l, h):
    if arr[i] <= pivotelement:
      arr[pivotindex], arr[i] = arr[i], arr[pivotindex]
      pivotindex += 1
  # Move the pivotelement to the pivotindex and return the pivotindex, pivotelement is now at it's correct place
  arr[pivotindex], arr[h] = arr[h], arr[pivotindex]
  # At this point all the elements to left of pivotindex are <= pivotelement and those at right are > pivotelement
  # Return the pivotindex
  return pivotindex


def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  # Push the initial low and high indexes to the stack
  stack.append(l)
  stack.append(h)
  # Pop the stack and make partitions in array until the stack is empty
  while stack:
    high = stack.pop()
    low = stack.pop()
    pivotindex = partition(arr, low, high)
    # If there are elements to the left of the pivotindex, then push the low and high indexes of the left subarray to the stack
    if pivotindex - 1 > low:
      stack.append(low)
      stack.append(pivotindex-1)
    # If there are elements to the right of the pivotindex, then push the low and high indexes of the right subarray to the stack
    if pivotindex + 1 < high:
      stack.append(pivotindex+1)
      stack.append(high)
