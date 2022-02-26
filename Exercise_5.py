# Python program for implementation of Quicksort

# This function is same in both iterative and recursive

def partition(arr, l ,h):
  #write your code here
  start = l
  end = h
  pivot = arr[l]
  pivot_index = l

  while(start<end):
      while start<len(arr) and arr[start] <= pivot:
          start = start + 1
      while arr[end] > pivot:
          end = end - 1
      if start < end:
          tmp1 = arr[start]
          arr[start]  = arr[end]
          arr[end] =  tmp1
          
  tmp2 = arr[end]
  arr[end] = arr[pivot_index]
  arr[pivot_index] = tmp2

  return end

def quickSortIterative(arr,l,h):
    #create a stack
    stack = [0] * (h)
    top = 0
  
    # push l and h to stack
    stack[top] = l
    top = top + 1
    stack[top] = h
  
    # Keep popping from stack while is not empty
    while top >= 0:
  
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
  
        p = partition( arr, l, h )

        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
  
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1)
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 