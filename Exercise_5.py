# Time Complexity : O(n^2) for worst case which is rare, O(nlogn) for average case
# Space Complexity : O(n) auxiliary space complexity as extra space is needed for the stack.
#                    O(n) overall space complexity as space is taken for array and stack both of which are of size n.
# Did this code successfully run on Leetcode : Code ran successfully.
# Any problem you faced while coding this : No problems

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h] # Making pivot as the last element
  ptr = l # Make the pointer start at index low
  for i in range(l,h+1): # Loop in range of all indexes from low to high including high
      if arr[i] <= pivot:
          arr[i], arr[ptr] = arr[ptr], arr[i] # Swap values at current ptr and i
          if i!= h:
              ptr+=1 # Increment ptr for next iteration except if it is the last i.e rightmost index
  return ptr


def quickSortIterative(arr, l, h):
  #write your code here

  stack = [] # We create a new stack to implement iterative quicksort
  
  stack.append(l) # We push l and h initially as we intend to sort in the range from l to h
  stack.append(h)

  while(stack):
    h = stack.pop() #While the stack is not empty we keep popping the left and right values and try to sort within the range
    l = stack.pop()

    ptr = partition(arr,l,h) # We make the partition between l and h

    if ptr-1 > l:
      stack.append(l) # If the left side of the partition is unsorted then we aim to sort that ...
      stack.append(ptr-1) # ... by pushing the values of leftmost element and the element before the partition 
    if ptr+1 < h:
      stack.append(ptr+1) # If the right side of the partition is unsorted then we aim to sort that ... 
      stack.append(h) # ... by pushing the values of the element after the partition and the rightmost element

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  