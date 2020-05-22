# Time Complexity :O(nLog(n))
# Space Complexity :O(Log(n))
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no


# Your code here along with comments explaining your approach
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  Pivot = arr[h]
  PivotIndex = l

  for i in range(l,h):
    if arr[i] <= Pivot:
      temp = arr[i]
      arr[i] = arr[PivotIndex]
      arr[PivotIndex] = temp
      PivotIndex +=1
  temp = arr[h]
  arr[h] = arr[PivotIndex]
  arr[PivotIndex] = temp
  return PivotIndex

def quickSortIterative(arr, l, h):
  stack = []
  stack.append(l)
  stack.append(h)
  while stack:
    high = stack.pop()
    low = stack.pop()
    p = partition(arr,low,high)
    if p > low:
      stack.append(low)
      stack.append(p-1)
    if p < high:
      stack.append(p+1)
      stack.append(high) 


arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 