# Python program for implementation of Quicksort
from collections import deque
# This function is same in both iterative and recursive
# Time complexity: O(nlogn)
# give you explanation for the approach
def partition(arr,l,h):
    #write your code here
    # i is variable which defines accurate position of pivot
    i = l-1
    # pivot is last element
    pivot = arr[h]
    # loop from low to high and swap element is smaller ( basic concept: el before pivot -> small.. el after pivot -> larger)
    for j in range(l,h):
       if arr[j]<= pivot:
           i += 1
           arr[i],arr[j] = arr[j] , arr[i]

    arr[i+1],arr[h] = arr[h],arr[i+1]
    return i+1


def quickSortIterative(arr, l, h):
  #write your code here
  # create a stack for storing sublist start and end index
  stack = deque()

  # get the starting and ending index of a given list
  start = l
  end = h

  # push the start and end index of the array into the stack
  stack.append((start, end))

  # loop till stack is empty
  while stack:

      # remove top pair from the list and get sublist starting
      # and ending indices
      start, end = stack.pop()

      # rearrange elements across pivot
      pivot = partition(arr, start, end)

      # push sublist indices containing elements that are
      # less than the current pivot to stack
      if pivot - 1 > start:
          stack.append((start, pivot - 1))

      # push sublist indices containing elements that are
      # more than the current pivot to stack
      if pivot + 1 < end:
          stack.append((pivot + 1, end))

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 