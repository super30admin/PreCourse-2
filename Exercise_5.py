# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(array, low, high):
  #write your code here
  i = ( low - 1 )
  x = array[high]
 
  for j in range(low , high):
    if   array[j] <= x:
      i = i+1
      array[i],array[j] = array[j],array[i]
 
  array[i+1],array[high] = array[high],array[i+1]
  return (i+1)


def quickSortIterative(array, low, high):

  #write your code here

  size = high - low + 1
  stack = [0] * (size)

  top = -1

  top = top + 1
  stack[top] = low
  top = top + 1
  stack[top] = high

  # Keep popping from stack while is not empty
  while top >= 0:

      # Pop high and low
    high = stack[top]
    top = top - 1
    low = stack[top]
    top = top - 1

    # sorted array
    p = partition( array, low, high )

    # push left side to stack
    if p-1 > low:
      top = top + 1
      stack[top] = low
      top = top + 1
      stack[top] = p - 1

    #  push right side to stack
    if p+1 < high:
      top = top + 1
      stack[top] = p + 1
      top = top + 1
      stack[top] = high

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
  print ("%d" %arr[i])
  
