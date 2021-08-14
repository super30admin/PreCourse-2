# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot=arr[l]
  i=l+1
  j=h
  while True:
    while(i<=j and pivot>=arr[i]):
      i=i+1
    while(i<=j andpivot<=arr[j]):
      j=j-1
    if i<=j:
      arr[i],arr[j]=arr[j],arr[i]
    else:
      break
  arr[j],arr[l]=arr[l],arr[j]

  return j
def quickSortIterative(arr, l, h):
  #write your code here

