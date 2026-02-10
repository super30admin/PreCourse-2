# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i=l-1
  j=l

  while j<=h:
    if arr[j]<=pivot:
      i+=1
      tmp = arr[i]
      arr[i] = arr[j]
      arr[j] = tmp
    j+=1
  return i


def quickSortIterative(arr, l, h):
  #write your code here
  stack = [0] * len(arr)
  stack.append(l)
  stack.append(h)

  while len(stack) > 0:
    high = stack.pop()
    low = stack.pop()
    pivotIndex = partition(arr, low, high)

    if pivotIndex - low >0:
      stack.append(low)
      stack.append(pivotIndex-1)

    if high - pivotIndex > 0:
      stack.append(pivotIndex+1)
      stack.append(high)

arr = [3, 2, 1, 4]
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
