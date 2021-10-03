# Time Complexity :O(n log N) or O(n ^2)
# Space Complexity :O(n)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this :No 

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  i = ( l - 1 )
  val = arr[h]
  
  for j in range(l , h):
      if   arr[j] <= val:
        i = i+1
        arr[i],arr[j] = arr[j],arr[i]
  
  arr[i+1],arr[h] = arr[h],arr[i+1]
  return (i+1)


def quickSortIterative(arr, l, h):
  #write your code here
    s = h - l + 1
    stack = [0] * (s)
    hi = -1
    hi = hi + 1
    stack[hi] = l
    hi = hi + 1
    stack[hi] = h
    while hi >= 0:
        h = stack[hi]
        hi = hi - 1
        l = stack[hi]
        hi = hi - 1
        p = partition( arr, l, h )
        if p-1 > l:
            hi = hi + 1
            stack[hi] = l
            hi = hi + 1
            stack[hi] = p - 1
        if p+1 < h:
            hi = hi+ 1
            stack[hi] = p + 1
            hi = hi + 1
            stack[hi] = h
  

arr = [18,5,34,3,2,3]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),

