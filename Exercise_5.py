# Python program for implementation of Quicksort

#Time Complexity: O(nlog(n))
#Space Complexity: O(n)

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l - 1
  for j in range(l,h):
    if arr[j]<=pivot:
      i = i + 1
      arr[i], arr[j] = arr[j], arr[i]
      
  arr[i+1], arr[h] = arr[h], arr[i+1]
  return i+1

def quickSortIterative(arr, l, h):
  #write your code here
  size = h - l + 1
  stack = [0] * size
  
  top = - 1
  
  top = top + 1
  stack[top] = l
  top = top + 1
  stack[top] = h
  
  while (top >= 0):
    h = stack[top]
    top -= 1
    l = stack[top]
    top -= 1

    # Set pivot element at its correct position in sorted array
    p = partition(arr, l, h)

    # If there are elements on the left side of the pivot, push them to the stack
    if p - 1 > l:
      top += 1
      stack[top] = l
      top += 1
      stack[top] = p - 1

        # If there are elements on the right side of the pivot, push them to the stack
    if p + 1 < h:
      top += 1
      stack[top] = p + 1
      top += 1
      stack[top] = h
      
arr= [10, 11, 3, 4, 12, 13]
n = len(arr)

quickSortIterative(arr, 0, n-1)

print(arr)
  
     
  
  

