# Python program for implementation of Quicksort
from collections import deque

# This function is same in both iterative and recursive
# time complexity for iterative quicksort is O(nlogn)
def partition(arr, l, h):
  #write your code here  
    pivot = arr[h];
    i = l-1;

    for j in range(l,h):
    #check element smaller than pivot 
      if(arr[j]<=pivot):
        i = i+ 1
        arr[i],arr[j] = arr[j],arr[i]
    
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)

def quickSortIterative(arr, l, h):
  #write your code here
  #Creating a stack 
  stack = deque()

  #Storing the start and end index in the stack
  stack.append((l,h))

  #Loop till stack is empty
  while stack:

    #Getting starting and ending indices
    start ,end= stack.pop()

    #Calling the partition function
    pivot = partition(arr,start,end)

    #Pushing the items less than the pivot onto the stack
    if pivot -1 > start:
      stack.append((start,pivot-1))
    
    #Pushing the items greater than the pivot onto the stack
    if pivot + 1 <end:
      stack.append((pivot + 1,end))


# Iterative Implementation of Quicksort
if __name__ == '__main__':
 
    arr = [9, -3, 10, -2, 6, 19, -6, 1, 4]
 
    len = len(arr)
    quickSortIterative(arr,0,len-1)
 
    # print the sorted list
    print(arr)





