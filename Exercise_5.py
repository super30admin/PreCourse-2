# Python program for implementation of Quicksort
# TC: O(N**2)
# SC: O(1)
def partition(arr, low, high):
  # This function is same in both iterative and recursive
    pivot = arr[low]
    i,j = low,high

    while i < j:
        
        while i < len(arr) and arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[low],arr[j] = arr[j],arr[low]

    return j


def quickSortIterative(arr, low, high):
  # creating an auxillary stack for storing intermediate values of low and high
  size = high-low + 1
  stack = [0]*size
  top = -1

  # Initializing the stack with initial values of low and high
  top += 1
  stack[top] = low
  top += 1
  stack[top] = high

  # keep popping the stack until not empty
  while top>=0:
    h = stack[top]
    top -= 1
    l = stack[top]
    top -= 1

    p = partition(arr,l,h)

    if p-1 > l:
      top += 1
      stack[top] = l
      top += 1
      stack[top] = p-1
  
    
    if p+1 < h:
      top += 1
      stack[top] = p+1
      top += 1
      stack[top] = h

arr = [9, -3, 5, 2, 6, 8, -6, 1, 3]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("Sorted array is:",*arr)


