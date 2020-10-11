# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  i = l-1
  pivot=arr[h]
  for j in range(l,h):
      if arr[j]<=pivot:
          i+=1
          arr[i],arr[j]=arr[j],arr[i]
  arr[i+1],arr[h]=arr[h],arr[i+1]
  return i+1

def quickSortIterative(arr, l, h):
  #instead of recursive calls to left and right side of elements of pivot, we will use a stack

  s =[0]*len(arr)
  top=-1

  #push l and h to stack
  top+=1
  s[top]=l
  top+=1
  s[top]=h

  while top>=0:
      #pop elements of stack to l and h
      h=s[top]
      top-=1
      l=s[top]
      top-=1
      pivot = partition(arr,l,h)

      #if there are elements to left of pivot push them(start and end point) to stack
      if pivot-1 > l:
          top+=1
          s[top]=l
          top+=1
          s[top]=pivot-1
      #simmilarly if there are elements right push the start and end points to stack

      if pivot+1 < h:
          top+=1
          s[top]=pivot+1
          top+=1
          s[top]=h


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),


#Time complexity: O(nlogn)
