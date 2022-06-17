# Python program for implementation of Quicksort
#Time Complexity: O(nlogn)
#Space Complexity: O(logn)


# This function is same in both iterative and recursive
def partition(arr, l, h):
  k = ( l - 1 )
  num = arr[h]
  
  for j in range(l , h):
        if   arr[j] <= num:
            # increment index of smaller element
            k = k+1
            arr[k],arr[j] = arr[j],arr[k]
  
  arr[k+1],arr[h] = arr[h],arr[k+1]
  return (k+1)


def quickSortIterative(arr, l, h):
  size = h - l + 1
  stack = [0] * (size)
  
  # initialize top of stack
  top = -1
  
  # push initial values of l and h to stack
  top = top + 1
  stack[top] = l
  top = top + 1
  stack[top] = h
  
  # Keep popping from stack while is not empty
  while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        p = partition( arr, l, h )
  
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

arr = [40, 20, 45, 65, 10, 33, 25, 39]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),

