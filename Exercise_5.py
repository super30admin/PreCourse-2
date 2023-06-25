# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot=arr[l]
  i=l+1
  j=h

  while True:
      while i<=j and arr[i]<=pivot:
          i+=1
      while i<=j and arr[j]>=pivot:
          j-=1
      if i<=j:
          arr[i],arr[j]=arr[j],arr[i]
      else:
          break
      
  arr[l],arr[j]=arr[j],arr[l]

  return j


def quickSortIterative(arr, l, h):
    size = h - l + 1
    stack = [0] * (size)
    top = -1
 
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0:
 
        # Pop both high and low out
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
 
        p = partition( arr, l, h )

        # left side onto stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        # right side onto stack
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 