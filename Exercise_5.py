# Python program for implementation of Quicksort
# Time Complexity : Average: O(Nlog(N)) worst: O(N^2)
# Space Complexity : O(log(N))

# This function is same in both iterative and recursive
def partition(arr, low, high):
  pivot = arr[int((low+high)/2)] # middle element is taken as pivot
    # swap elements to left and right of pivot that are out of order
  while low <= high:
    while arr[low] < pivot: 
        low += 1
    while arr[high] > pivot:
        high -= 1
    
    if low <= high: # low and high is not crossed
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
  # low will be the pivot index
  return low  


# sort
def quickSortIterative(arr,l,h):
   # stack in place of recursion
   size = h - l + 1
   stack = [0] * (size)
   top = -1
   # push initial values
   top += 1
   stack[top] = l
   top += 1
   stack[top] = h
   # pop from stack
   while top >= 0:
      # Pop
      h = stack[top]
      top -= 1
      l = stack[top]
      top -= 1
      # Set pivot element at its correct position
      p = partition( arr, l, h )
      # elements on the left
      if p-1 > l:
         top = top + 1
         stack[top] = l
         top = top + 1
         stack[top] = p - 1
      # elements on the right
      if p+1 < h:
         top = top + 1
         stack[top] = p + 1
         top = top + 1
         stack[top] = h


arr = [8,6,5,4,7]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("Sorted array is:", arr)