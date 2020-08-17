# Python program for implementation of Quicksort
# Iterative quick sort can be implemented in the same way as recusive call stack.
# Use auxillary call stack to keep the values of low and high pointers.
# Time complexity - O(n logn)
# Space complexity - O(logn)

from collections import deque
# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  j = l - 1

  for i in range(l, h):
  	# if the element at ith location is less than pivot, swap elements at ith and jth location.
  	if arr[i] <= pivot:
  		j+=1
  		arr[j], arr[i] = arr[i], arr[j]

  arr[j+1], arr[h] = arr[h], arr[j+1]
  return j+1	# return the new position of the pivot


def quickSortIterative(arr, l, h):
  #write your code here
  stack = deque()
  stack.append((l, h))
  while stack:
  	l, h = stack.pop()
  	pivotloc = partition(arr, l, h)
  	# Add the right subarray locations to the stack. From left to the pivot_loc - 1.
  	if pivotloc+1<=h:
  		stack.append((pivotloc+1, h))
  	# Add the left subarray locations to the stack. From pivot_loc + 1 to the right.
  	if l<pivotloc:
  		stack.append((l, pivotloc-1))
  	


 # Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
print ("Original array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]) 
