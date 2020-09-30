# Python program for implementation of Quicksort

import random
# give you explanation for the approach - Using same partitioning scheme as recursive quicksort
def partition(arr,start,end):
    random_pivot_index = random.randint(start, end)
    arr[random_pivot_index], arr[start] = arr[start], arr[random_pivot_index]
    pivot = arr[start]
    orange = start
    for green in range(start + 1, end + 1):
        if arr[green] <= pivot:
            orange += 1
            arr[orange], arr[green] = arr[green], arr[orange]
            
    arr[start], arr[orange] = arr[orange], arr[start]
    return orange

# Remove recursion using and implict stack
def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  start = 0
  end = len(arr) - 1
  
  stack.append((start, end))
  
  while stack:
        start, end = stack.pop()
        p = partition(arr, start, end)
        if p - 1 > start:
              stack.append((start, p - 1))
        if p + 1 < end:
              stack.append((p + 1, end))
              
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 