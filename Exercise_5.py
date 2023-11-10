# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
#Time complexity: O(nlogn)
#Space complexity: O(n)
def partition(arr, low, high):
  #write your code here
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1    



def quickSortIterative(arr, l, h):
  size = h - l + 1
  stack = [0] * (size)
  top = -1
  top = top + 1
  stack[top] = (l,h)
  while top >= 0:
      l,h = stack[top]
      top = top - 1
      p = partition( arr, l, h )
      if p-1 > l:
          top = top + 1
          stack[top] = (l,p-1)

      if p + 1 < h:
          top = top + 1
          stack[top] = (p+1,h)
arr=[10, 7, 8, 9, 1, 5]
quickSortIterative(arr,0,5)
print(arr)
