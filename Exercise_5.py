# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  max_pos = l
  for i in range(l,h+1):
    if arr[i] <= pivot:
      temp = arr[max_pos]
      arr[max_pos] = arr[i]
      arr[i] = temp
      max_pos += 1
  return max_pos-1

def quickSortIterative(arr, l, h):
  #write your code here
    if l < h:
      stack = []
      stack.append((l,h))
      while stack:
        l, h = stack.pop()
        partition_pos = partition(arr, l, h)
        if partition_pos - 1 > l:
           stack.append((l, partition_pos - 1))
        if partition_pos + 1 < h:
           stack.append((partition_pos + 1, h))
      

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  