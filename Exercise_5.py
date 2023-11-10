# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot=arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1


def quickSortIterative(arr, l, h):
  #write your code here
  length=h-l+1
  st=[0]*(length)
  top=-1
  top=top+1
  st[top]=l
  top=top+1
  st[top]=h
  while top>=0:
    h=st[top]
    top=top-1
    l=stack[top]
    top=top-1
    pi=partition(arr,l,h)
    if pi-1>l:
      top=top+1
      st[top]=l
      top=top+1
      st[top]=pi-1
    if pi+1<h:
      top=top+1
      st[top]=pi+1
      top=top+1
      st[top]=h


