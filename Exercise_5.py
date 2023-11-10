# Python program for implementation of Quicksort

# // Time Complexity : O(lg n) where n is the number of elements in the array
  # // Space Complexity : O(lg n) where n is the number of elements in the array 
  # for which recursive calls were made
  # // Did this code successfully run on Leetcode : yes
  # // Any problem you faced while coding this : a little when writing the 'terminating condition'
  # if l > r:
  #       return -1

  # // Your code here along with comments explaining your approach

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  i = l-1
  pivot = arr[h]
  for j in range(l,h):
    if arr[j] <= pivot:
      i += 1
      arr[i],arr[j] = arr[j],arr[i]
  arr[i+1],arr[h] = arr[h],arr[i+1]
  return i+1

def quickSortIterative(arr, l, h):
  #write your code here
  if l < h:
    index = partition(arr,l,h)
    quickSortIterative(arr,l, index-1)
    quickSortIterative(arr, index+1,h)
  
arr = [2,8,7,1,3,5,6,4]
print(quickSortIterative(arr,0,len(arr)-1))

