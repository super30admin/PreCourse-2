# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivotIndex=l
  i=l
  j=h

  while i<j:
    while i<len(arr) and arr[i]<=arr[pivotIndex]:
      i+=1
    while arr[j]>arr[pivotIndex]:
      j-=1
    if i<j:
      arr[i],arr[j]=arr[j],arr[i]
  arr[j],arr[pivotIndex]=arr[pivotIndex],arr[j]
  return j


def quickSortIterative(arr, l, h):
  #write your code here
  st=[0]*(h-l+1)

  top=-1
  
  top+=1
  st[top]=l
  top+=1
  st[top]=h

  while top>=0:
    h=st[top]
    top-=1
    l=st[top]
    top-=1

    p=partition(arr,l,h)

    if p-1>l:
      top+=1
      st[top]=l
      top+=1
      st[top]=p-1
    if p+1<h:
      top+=1
      st[top]=p+1
      top+=1
      st[top]=h
  

#time Complexity: O(n log n)
#space complexity: O(log n)
