# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  i = l-1
  j = arr[h]
  
  for k in range(l, h):
    if arr[k] <= j:
      i += 1
      arr[i], arr[k] = arr[k], arr[i]
  arr[i+1], arr[h] = arr[h], arr[i+1]
  return i+1


def quickSortIterative(arr, l, h):
  #write your code here
  s_len = h-l+1
  stack = [0]*s_len
  
  top = -1 #initializing top of stack
  
  #pushing to stack
  top = top+1
  stack[top] = l
  top = top+1
  stack[top] = h
  
  while top >= 0:
    #pop from stack
    h = stack[top]
    top = top-1
    l = stack[top]
    top = top-1
    
    x = partition(arr, l, h) # setting pivot element in sorted array

    # pushing left side elements of pivot to stack
    if x-1 > l:
        top = top+1
        stack[top] = l
        top = top+1
        stack[top] = x-1
    
    # pushing right side elements of pivot to stack 
    if x+1 < h:
        top = top+1
        stack[top] = x+1
        top = top+1
        stack[top] = h
  
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
