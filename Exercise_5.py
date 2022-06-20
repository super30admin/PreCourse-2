'''
# Exercise_5 : # Python program for implementation of Quicksort Iterative.

# Description: Quick sort iterative algorithm.

# Author: Neha Doiphode
# Date  : 06-19-2022

# Approach:
    Please refer to comments added in the code below.

# Time Complexity                            : Please refer to exercise 2.
# Space Complexity                           : Please refer to exercise 2.
# Did this code successfully run on Leetcode : Did not run on leetcode.
# Any problem you faced while coding this    : Nothing critical.
'''

# This function is same in both iterative and recursive
def partition(arr, l, h):

     # Initialize index to traverse. Set it prior to low
     i = l - 1

     # Choosing pivot as last element
     pivot = arr[h]

     for j in range(l, h):
         if arr[j] <= pivot:
             i += 1

             # Keep swapping elements lesser than pivot to the left
             arr[i], arr[j] = arr[j], arr[i]

     # i will stop at the element smaller than pivot.
     # Hence, we need to move pivot to position i+1 such that,
     # all elements smaller than pivot will be to its left and greater will be to its right
     arr[i + 1], arr[h] = arr[h], arr[i+1]
     return i+1


def quickSortIterative(arr, l, h):

    # Any iterative implementation would need a stack.
    # initialize stack/list as we are going to access indices of the list by moving top of the stack defined next.
    stack = [0] * len(arr)

    # initializing top of stack
    top = l - 1 # top = -1

    # push initial set of values onto the stack
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    # Now start looping
    # Condition: loop until stack is not empty
    while top >= 0:

        # pop items from the stack
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        # Now, partition the array with partition method
        partition_index = partition(arr, l, h)

        # Repeat the process to the left of partition index and to the right of partition index
        # if there are elements present to the left and present to the right
        if partition_index - 1 > l: # Means there are elements present to the left of partition index
            top += 1
            stack[top] = l
            top += 1
            stack[top] = partition_index - 1

        if partition_index + 1 <  h:
            top += 1
            stack[top] = partition_index + 1
            top += 1
            stack[top] = h


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
#arr = [5, 4, 3, 2, 1]
n = len(arr)
quickSortIterative(arr,0,n-1)
print (f'Sorted array is: {arr}')
