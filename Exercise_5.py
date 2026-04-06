# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
  #write your code here
  pivot = arr[low]
  left = low
  for i in range(low+1,high+1):
    if arr[i] < pivot:
      left+=1
      arr[i],arr[left] = arr[left], arr[i]

  arr[low],arr[left] = arr[left],arr[low]
  return left 


def quickSortIterative(arr):
  #write your code here
  size = len(arr)
  stack = [(0,size-1)]

  while stack:
    low,high = stack.pop()

    p = partition(arr,low,high)

    if p-1 > low:
      stack.append((low,p-1))

    if p+1 < high:
      stack.append((p+1,high))

arr = [10, 7, 8, 9, 1, 5]
quickSortIterative(arr)
print("Sorted array:", arr)


# stack = [(0,5)]
# low = 0, high = 5
# p = partition(arr,0,5)