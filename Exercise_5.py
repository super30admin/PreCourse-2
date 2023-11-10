# Python program for implementation of Quicksort

# Time Complexity : o(nlogn) (Average Case Complexity)
# Space Complexity : o(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

def partition(arr,l,h):
    i = ( l - 1 )
    x = arr[h]
    for j in range(l , h):
        if   arr[j] <= x:
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)

def quickSortIterative(arr,l,h):
  # Create an auxiliary stack
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
    # Pop h and l
    h = stack[top]
    top = top - 1
    l = stack[top]
    top = top - 1
    # Set pivot element at its correct position in
    # sorted array
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

example = [4, 5, 1, 2, 3]
result = [1, 2, 3, 4, 5]
print(quickSortIterative(example, 0, len(example)-1))
 
example = [2, 5, 6, 1, 4, 6, 2, 4, 7, 8]
result = [1, 2, 2, 4, 4, 5, 6, 6, 7, 8]

print(quickSortIterative(example, 0, len(example)-1))

#Output 
#[1, 2, 3, 4, 5]
#[1, 2, 2, 4, 4, 5, 6, 6, 7, 8]