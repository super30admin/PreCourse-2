# Python program for implementation of Quicksort

#TC = o(nlogn)
#SC = o(n)

# This function is same in both iterative and recursive
def partition(arr, low, high):
  l = low
  h = high -1
  pvt = arr[high]
  while l < h:
      while l < high and arr[l] < pvt:
          l += 1
      while h > low and arr[h] >= pvt:
          h -= 1
      if l < h:
          arr[l], arr[h] = arr[h], arr[l]
  if arr[l] > pvt:
      arr[l], arr[high] = arr[high], arr[l]
  return l   


def quickSortIterative(arr, l, h):
  n = h - l + 1 # to create stack of size n 
  upstack = [0]*(n//2+1)  
  lowstack = [0]*(n//2+1) 
  top = 0

  top += 1
  lowstack[top] = l
  upstack[top] = h

  while top >= 0:
        h = upstack[top]
        l = lowstack[top]
        top -= 1
        p = partition( arr, l, h )

        if p-1 > l:
            top += 1
            lowstack[top] = l
            upstack[top] = p - 1

        if p+1 < h:
            top += 1
            lowstack[top] = p + 1
            upstack[top] = h

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 