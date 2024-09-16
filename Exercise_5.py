# Python program for implementation of Quicksort
from collections import deque
# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = h
  i = l
  j = l
  while(i<h):
      if(arr[i]<arr[pivot]):
          arr[i],arr[j] = arr[j],arr[i]
          j+=1
      i+=1
  arr[pivot],arr[j] = arr[j],arr[pivot]
  return j


def quickSortIterative(arr, l, h):
  #write your code here
  stack = deque([[l,h]])
  while(len(stack)>0):
    l1,h1 = stack.popleft()
    if(l1>=h1):
      continue
    pivot = partition(arr,l1, h1)
    stack.append([l1,pivot-1])
    stack.append([pivot+1,h1])

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),