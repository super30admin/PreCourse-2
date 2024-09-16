# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  '''
   Considers pivot as last element (did not use temp
   variable for interchanging)
   This function places all elements less than pivot
   to its left and greater than pivot on its right
   '''
  i = l - 1
  pivot = arr[h]
  for j in range(l, h):
      if arr[j] < pivot:
          i = i + 1
          arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return (i + 1)


# write your code here
def quickSortIterative(arr, l, h):
  '''
  Create a stack and push the low and high
  values into the stack.
  Iterate through the stack, pop two
  elements in stack and call partition,
  check if partition-1> low value, if yes
  push left Sub array indexes from the partition
  into the stack else if partition+1< high
  then push right array sub indexes in stack.
  Next iteration pop 2 elements from stack and
  repeat this until top == -1.
  Time Complexity : O(n^2)
  Space Complexity: O(log n)
  '''

  size = h - l + 1
  stack = [0 for x in range(0,size)]

  top = -1
  top = top + 1
  stack[top] = l
  top = top + 1
  stack[top] = h

  while top >= 0:

      h = stack[top]
      top = top - 1
      l = stack[top]
      top = top - 1

      p = partition(arr, l, h)

      if p - 1 > l:
          top = top + 1
          stack[top] = l
          top = top + 1
          stack[top] = p - 1

      if p + 1 < h:
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

