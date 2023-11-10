#Time Complexity: O(nlogn)
#Space Complexity: O(n)
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  i = l-1
  pivot = arr[h]
  for j in range(l,h):
    if arr[j]<=pivot:
      i+=1
      arr[i],arr[j] = arr[j],arr[i]
  arr[i+1],arr[h]=arr[h],arr[i+1]
  return i+1

def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  stack.append(l)
  stack.append(h)
  while len(stack)>0:
    h = stack.pop()
    l = stack.pop()
    p = partition(arr,l,h)
    if p-1>l:
      stack.append(l)
      stack.append(p-1)
    if p+1<h:
      stack.append(p+1)
      stack.append(h)

