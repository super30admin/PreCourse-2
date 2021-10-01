# Python program for implementation of Quicksort
# This function is same in both iterative and recursive
def partition(arr, l, h):
  i=l-1
  pivot=arr[h]
  for j in range(l,h):
      if arr[j]<=pivot:
          i+=1
          arr[i],arr[j]=arr[j],arr[i]
  arr[i+1],arr[h]=arr[h],arr[i+1]
  return i+1


def quickSortIterative(arr, l, h):
  #Create a stack 
  size=h-l+1
  stack=[0]*size
  #initialize top
  top=-1
  #Push the lower and higher indices onto the stack
  top+=1
  stack[top]=l
  top+=1
  stack[top]=h
  #Pop till stack is not empty
  while top>0:
    h=stack[top]
    top-=1
    l=stack[top]
    top-=1
    #Set the pivot element in correct position
    p=partition(arr,l,h)
    #Push left subarray to stack if elements are present
    if p-1>l:
      top+=1
      stack[top]=l
      top+=1
      stack[top]=p-1
    #Push to right subarray to stack if elements are present
    if p+1<h:
      top+=1
      stack[top]=p+1
      top+=1
      stack[top]=h


arr=[4,3,5,2,1,3,2,3]
n=len(arr)
quickSortIterative(arr,0,n-1)
print("Sorted array is ")
for i in range(n):
  print("%d" %arr[i])


