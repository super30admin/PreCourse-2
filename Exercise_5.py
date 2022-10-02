# Time Complexity : O (nlogn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this : Coding the iterative part was difficult. 

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  # we will take the first element of the array as the pivot value
    pivot = arr[l]
    # Pointers for the left end and right ends of the array
    i = l
    j = h
    # loop through until i crosses j
    while i < j:
        #  Increment the value of i until we find an element greater than the pivot 
        while i < j and arr[i]<= pivot:
            i = i+1
        # Decrement the value of j while we find an element less than the pivot
        while arr[j]>pivot:
            j = j-1
        # Swap those two elements
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    # Swap the pivot with the element at the j pointer. 
    arr[l],arr[j] = arr[j], pivot
    # return the pivot index.
    return j


def quickSortIterative(arr, l, h):
  # Instead of using recursion, we will use iteration.
  # We will use a stack to perform this operation.
  length = (h-l)+1
  stack = [0] * length
  # we will initialize the top of the stack, which is the last element of the list.
  high = -1
  # we will push the current values of the two pointers l and h
  high = high +1
  stack[high] = l
  high = high+1
  stack[high] = h

  # we will keep popping from the stack while it is not empty
  while high>=0:
    # We will pop the values of h and l
    h = stack[high]
    high = high-1
    l = stack[high]
    high = high-1

  # We will find the pivot index 
    pi = partition(arr, l, h)

    # We will push the left side of the pivot value to the stack
    if pi-1>l:
      high = high+1
      stack[high] = l
      high = high+1
      stack[high] = pi-1
    # We will push the right side of the pivot value to the stack.
    if pi+1<h:
      high = high+1
      stack[high] = pi+1
      high = high+1
      stack[high] = h

arr = [100, 200, 300, 432, 1, 23, 45, 67]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
	print ("%d" %arr[i]),





