# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, start, end):
  pivot = arr[end]
  i = start-1

  for j in range(start,end):
    if(arr[j] < pivot):
      i+=1
      arr[i],arr[j] = arr[j],arr[i]
  arr[i+1],arr[end] = arr[end],arr[i+1]
  return i+1
  #write your code here


def quickSortIterative(arr):
  #write your code here

  stack = [(0,len(arr)-1)]

  while stack:
    start,end = stack.pop()
    if start >= end:
      continue

    pindex = partition(arr,start,end)
    stack.append((start,pindex-1))
    stack.append((pindex+1,end))


arr = [1,3,2,5,10,2]
quickSortIterative(arr)
print(arr)