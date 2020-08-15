# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[l]
  start = l + 1
  end = h
  
  while True:
    while start <= end and arr[start] <= pivot:
      start += 1
    while start <= end and arr[end] > pivot:
      end -= 1
    if start <= end:
      arr[start], arr[end] = arr[end], arr[start]
    else:
      break
  arr[end], arr[l] = arr[l], arr[end]
  return end


def quickSortIterative(arr, l, h):
  #write your code here
  if l >= h:
    return
  stack = [(l,h)]

  while stack:
    low, high = stack.pop()
    p = partition(arr, low, high)

    if p > low:
      stack.append((low, p - 1))
    
    if p > high:
      stack.append((p + 1, high))

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 