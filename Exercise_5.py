# Time Complexity : O(n^2)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no

# Your code here along with comments explaining your approach

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  i = ( l - 1 )
    x = arr[h]

    for j in range(l , h):
        if   arr[j] <= x:
            i = i+1 # incrementing index of smaller element
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)


def quickSortIterative(arr, l, h):
  #write your code here
  size = h - l + 1 # Creating a stack
    stack = [0] * (size)
    top = -1 # initializing top of stack
    top = top + 1 # pushing initial values of l and h to stack
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0: # popping from stack while is not empty

        h = stack[top] # popping h and l
        top = top - 1
        l = stack[top]
        top = top - 1

        p = partition( arr, l, h ) # setting pivot element at its correct position in sorted array

        if p-1 > l: # If there are elements on left side of pivot,then push left side to stack
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        if p+1 < h: # If there are elements on right side of pivot, then push right side to stack
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
