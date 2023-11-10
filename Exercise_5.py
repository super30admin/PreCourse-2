# Time Complexity : O(nlogn)
# Space Complexity : O(logn)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    #last index being taken as pivot, bigInx is the index of value greater than pivot
    bigInx = l-1
    pivot = arr[h]

    for smlInx in range(l,h):
        # if value less than pivot, values at smlInx and bigInx are interchanged
        if arr[smlInx] <= pivot:
            bigInx += 1
            arr[bigInx], arr[smlInx] = arr[smlInx], arr[bigInx]

    #finally pivot value and the index next to bigInx are interchanged
    arr[bigInx+1], arr[h] = arr[h], arr[bigInx+1]  
    return bigInx+1

# The idea is use a stack to keep track of the indices derived as pivots are found. During each iteration,
# the indices are popped and the same process is continued until stack is empty
def quickSortIterative(arr, l, h):
  stack = []
  start,end = 0,len(arr)-1

  stack += [(start,end)]
  
  while stack:
    start,end = stack.pop()
    pivot = partition(arr,start,end)

    if pivot - 1 > start:
      stack += [(start, pivot-1)]

    if pivot + 1 < end:
      stack += [(pivot+1, end)]

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 

