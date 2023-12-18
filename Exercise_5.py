# // Time Complexity : O(nlogn)
# // Space Complexity : O(n) since we are holding and low values in stack
# // Did this code successfully run on Leetcode : NA
# // Any problem you faced while coding this : None
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = (l+h)//2
  lesserThanPivot = l

  while l<=h:
      if arr[l] < arr[pivot]:
          arr[lesserThanPivot],arr[l] = arr[l],arr[lesserThanPivot]
          if lesserThanPivot == pivot:
              pivot = l
          lesserThanPivot += 1
      l += 1
      
  
  arr[lesserThanPivot],arr[pivot] = arr[pivot],arr[lesserThanPivot]

  return lesserThanPivot

def quickSortIterative(arr, l, h):
  #write your code here
  rangeStack = [(l,h)]

  while rangeStack:
     l,h = rangeStack.pop()

     if l<h:
        pivot1 = partition(arr,l,h)
        rangeStack.append((l,pivot1-1))
        rangeStack.append((pivot1+1,h))