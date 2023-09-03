# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  item= arr[h]
  i=l-1
  for  j in range(l,h):
    if arr[j]<item:
      i+=1
      arr[i], arr[j]=arr[j],arr[i]
  arr[i+1] , arr[h] = arr[h], arr[i+1]
  return i+1


def quickSortIterative(arr, l, h):
  #write your code here
  stack =[(0,len(arr)-1)]
  while stack:
    l, h= stack.pop()

    if l<h:
      i=partition(arr,l,h)
      stack.append((l,i-1))
      stack.append((i,h))



