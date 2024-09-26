# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  # 1. slecting last element as the pivot
  p = arr[h]
  # 2. set index of smaller element as i
  i = (l -1)
  # 3. Loop over j to compare it with p: if greater/equal, move i by one and swap: 
  # if smaller, do nothing
  for j in range(l, h):
      if arr[j] <= p:
          i=i+1
          arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[h] = arr[h], arr[i+1]
  return (i+1)


def quickSortIterative(arr, l, h):
  # creating a stack & initialise
  size = h - l + 1
  stack = [0] * (size) 
  top = -1

  # pushing initial values to stack 
  top += 1
  stack[top] = l 
  top += 1
  stack[top] = h 

  # Pop until stack is not empty
  while top >= 0: 
      h = stack[top] 
      top -= 1
      l = stack[top] 
      top -= 1

      # get the index of partition
      p = partition( arr, l, h ) 

      # do it for the left & right sides of partition
      if p-1 > l: 
          top += 1
          stack[top] = l 
          top += 1
          stack[top] = p - 1
      if p + 1 < h: 
          top += 1
          stack[top] = p + 1
          top += 1
          stack[top] = h
  
# Driver code to test above (from Exercise_2)
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 


