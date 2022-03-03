# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
from cmath import pi


def partition(arr, l, h):
  return
  #write your code here
    # i = l - 1
    # pivot = arr[h]
    # for j in range(l, h):
    #     if arr[j] <= pivot:
    #         i += 1
    #         arr[i], [j] = arr[j], arr[i]
    # arr[i+1], arr[h] = arr[h], arr[h+1]
    # return (i+1)

def quickSortIterative(arr):
  
  # pivot = high
  # lo = low
  # hi = high - 1

  n = len(arr) - 1
  lo = 0
  hi = n - 1
  pivot = n
  
  stack = [[lo, hi]]

  while(stack):
    high = stack[0][1]
    low = stack[0][0]
    
    if low == high or low >= high:
      break;
    # print(stack)
    pivot = n
    high = n - 1
    low = 0
    while (low < high):
      # if low value is less than pivot value then the low increments
      if arr[low] < arr [pivot]:
        low += 1
      # if high value is greater than pivot it decrements
      if arr[high] > arr[pivot]:
        high -= 1
      
      if arr[low] > arr[pivot] and arr[high] <= arr[pivot] and arr[low] != arr[pivot]:
        tmp = arr[high]
        arr[high] = arr[low]
        arr[low] = tmp
        low += 1
        high -= 1
        
    # tmp = arr[pivot] 
    # arr[pivot] = arr[high]
    arr.insert(high+1, arr.pop())
    # arr[high] = tmp
    print(arr)
    left = [lo, high]
    right = [high+2, hi]
    stack.append(left)
    stack.append(right)
    stack.pop(0)
  return arr
    # if l < h:
    #     partitionIndex = partition(arr, l, h)
        
    #     print(quickSortIterative(arr, l, partitionIndex-1))
    #     print(quickSortIterative(arr, partitionIndex+1, h))
  #write your code here 
  
arr = [3,343,4,45655,2,6,67,1,78,2,78]
# Calling quickSort function
print(quickSortIterative(arr))

