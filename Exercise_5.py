# Time Complexity :
# Space Complexity :
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this : Not sure how to do this


# Your code here along with comments explaining your approach

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):

  #write your code here
  pivot = arr[h]
  i = l - 1
  for j in range(l, h):
    if arr[j] <= pivot:
      i += 1
      (arr[i], arr[j]) = (arr[j], arr[i])
  (arr[h], arr[i + 1]) = (arr[i + 1], arr[h])
  return (i+1)

def quickSortIterative(arr, l, h):

  #write your code here

