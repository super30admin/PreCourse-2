# Python program for implementation of Quicksort

# Partition the array till the stack is empty by selecting a pivot. Bring all the values smaller than pivot to the left and greater than pivot to the right.
# Pop the first element in the stack everytime
# If p-1 is greater than low, push low and p-1 to the stack, if p+1 is less than high, push p+1 and high in the stack.
# Do this till the stack is empty

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

def partition(arr, l, h):
  pivot = arr[h]
  pIndex = l
  for i in range(l, h):
      if arr[i] <= pivot:
          arr[i], arr[pIndex] = arr[pIndex], arr[i]
          pIndex += 1
  arr[pIndex], arr[h] = arr[h], arr[pIndex]
  return pIndex

def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  stack.append(h)
  stack.append(l)
  while stack and len(stack) >1:
    l = stack[-1]
    h = stack[-2]
    stack.pop()
    p = partition(arr, l, h)
    if p-1 > l:
      stack.append(l)
      stack.append(p-1)
    if p+1 < h:
      stack.append(p+1)
      stack.append(h)


arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  