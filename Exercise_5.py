# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  pindex = l

  for i in range(l,h):
      if arr[i]<=pivot:
          arr[i],arr[pindex]=arr[pindex],arr[i]
          pindex=pindex+1
  
  arr[pindex],arr[h]=arr[h],arr[pindex]
  return pindex

def quickSortIterative(arr, l, h):
  #write your code here
  n = len(arr)
  top = 0
  lowerS = []
  upperS = []
  lowerS.append(0)
  upperS.append(n-1)

  while top>-1:
    start = lowerS[top]
    end = upperS[top]
    top-=1
    loc = partition(arr,start,end)

    if start<loc-1:
      top+=1
      lowerS[top]=start
      upperS[top]=loc-1
    
    if loc+1<end:
      top+=1
      lowerS[top]=loc+1
      upperS[top]=end

arr = [10, 7, 8, 9, 1, 5]
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 