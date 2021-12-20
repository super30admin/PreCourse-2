# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
  #write your code here
  pivot = arr[high]
  l = low -1
  
  for i in range(low, high):
      if arr[i] <= pivot:
          l = l+1
          arr[l], arr[i] = arr[i], arr[l] # swap 
  arr[l + 1], arr[high] = arr[high], arr[l+1]
  return l + 1


def quickSortIterative(arr, low, high):
  #write your code here
    size = high -low + 1
    stack = [0] * (size)
  
    # initialize top of stack
    top = -1
  
    # push initial values oflow andhigh to stack
    top = top + 1
    stack[top] =low
    top = top + 1
    stack[top] =high
  
    while top >= 0:
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
        p = partition(arr, low, high )
  
        if p-1 > low:
            top = top + 1
            stack[top] =low
            top = top + 1
            stack[top] = p - 1

        if p+1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1


arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 