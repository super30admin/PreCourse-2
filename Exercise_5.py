# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  i = l-1
  pivot = arr[h]
  for j in range(l,h):
    if arr[j]< pivot:
      i += 1
      arr[i],arr[j] = arr[j],arr[i]
  arr[i+1],arr[h] = arr[h],arr[i+1]
  return i+1
  
def quickSortIterative(arr, l, h):
  #write your code here
  n = len(arr)
  stack = [0]*n
  top = -1
  top = top+1
  stack[top] = (l,h)
  while top>=0:
    l,h = stack[top]
    top -= 1
    q = partition(arr,l,h)
    if q-1> l:
      top += 1
      stack[top] = (l,q-1)
    if q+1<h:
      top += 1
      stack[top] =(q+1,h)

arr = [9,7,6,5,3,2]
quickSortIterative(arr,0,5)
for el in arr:
  print(el)