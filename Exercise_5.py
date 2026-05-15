# Time Complexity : 
#     Average case: O(nlogn)
#     Worst case: O(n^2)
# Space Complexity :
#     Average case: O(logn)
#     Worst case: O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : 
#                     I was struggling to do it iteratively as could not understand how to keep track of the 
#                     sorted pivots and how to sort the pivots every time with a different range of elements
#                     in the array. Then I saw that I can use the partition funtion from previous implementation
#                     so I just used the white board to come up with the idea of storing the partitions which are unsorted.
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[l]
  leftwall = l + 1

  for j in range(l+1, h+1):
      if arr[j] <= pivot:
          arr[leftwall], arr[j] = arr[j], arr[leftwall]
          leftwall += 1
  
  arr[leftwall - 1], arr[l] = arr[l], arr[leftwall - 1]
  return leftwall - 1

def quickSortIterative(arr, l, h):
  #write your code here
  partitions = [(l, h)]
  while len(partitions) > 0:
      low, high = partitions.pop()
      p = partition(arr, low, high)
      if low < p-1:
          partitions.append((low, p-1))
      if high > p+1:
          partitions.append((p+1, high))