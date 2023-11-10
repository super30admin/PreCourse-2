# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
# time complexity: O(logn) 
# Space complexity: O(logn) 
def partition(arr, l, h):
  #write your code here
  i = l
  j = h - 1
  pivot = arr[h]
  while i < j:
    while i < h and arr[i] < pivot:
      i += 1
    while j > l and arr[j] > pivot:
       j -= 1
    if i < j:
       arr[i], arr[j] = arr[j], arr[i]
  if arr[i] > pivot:
     arr[i], arr[h] = arr[h], arr[i]
  return i

def quickSortIterative(arr, l, h):
  stack = [(0, len(arr)-1)]

  while stack:
    start, end = stack.pop()

    partition_pos = partition(arr, start, end)

    if partition_pos - 1 > start:
        stack.append((start, partition_pos-1))
      
    if partition_pos + 1 < end:
       stack.append((partition_pos+1, end))
  return arr
    

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 