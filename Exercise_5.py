# Time Complexity : O(n^2)
# Space Complexity : O(n) as a stack is used
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : I did not know how to do this. Had to refer into existing codes on the internet to learn.

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
    size = len(array)
    if size == 1:
      return
    stack = [0] * (size)
    top = 0
    stack[top] = low
    top += 1
    stack[top] = high
 
    # Keep popping from stack while is not empty
    while top >= 0:
 
        # Pop high and low
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1
 
        # sorted array
        p = partition( array, low, high )

        # push left side to stack
        if p-1 > low:
            top += 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        #  push right side to stack
        if p+1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high

array = [10, 7, 8, 9, 1, 5]
n = len(array)
print("Original Array:", array)
quickSortIterative(array, 0, n-1)
print ("Sorted Array :", array)