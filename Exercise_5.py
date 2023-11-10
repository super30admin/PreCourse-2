# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    #write your code here
    #choose the rightmost element as pivot
  pivot = arr[h]
  # pointer for greater element
  i = l - 1
  # traverse through all elements
  # compare each element with pivot
  for j in range(l, h):
    if arr[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1
      # swapping element at i with element at j
      (arr[i], arr[j]) = (arr[j], arr[i])

  # swap the pivot element with the greater element specified by i
  (arr[i + 1], arr[h]) = (arr[h], arr[i + 1])

  # return the position from where partition is done
  return i + 1

def quickSortIterative(arr, l, h):
  #write your code here
  size = h - l + 1
  stack = [0] * (size)
 
  top = -1
 
  top = top + 1
  stack[top] = l
  top = top + 1
  stack[top] = h
 
    # Keep popping from stack while is not empty
  while top >= 0:
 
        # Pop high and low
      h = stack[top]
      top = top - 1
      l = stack[top]
      top = top - 1
 
        # sorted array
      p = partition( arr, l, h )

        # push left side to stack
      if p-1 > l:
          top = top + 1
          stack[top] = l
          top = top + 1
          stack[top] = p - 1

        #  push right side to stack
      if p+1 < h:
          top = top + 1
          stack[top] = p + 1
          top = top + 1
          stack[top] = h
array = [9, 0, 8, 1, 7, 3, 6, 4]
n = len(array)
print("Orignal Array:", array)
quickSortIterative(array, 0, n-1)
print ("Sorted Array :", array)