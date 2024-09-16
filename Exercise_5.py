# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[l]
  leftwall = l + 1

  for i in range(l+1, h+1):
      if arr[i] < pivot:
          arr[i], arr[leftwall] = arr[leftwall], arr[i]
          leftwall += 1

  arr[l], arr[leftwall - 1] = arr[leftwall - 1], arr[l]

  return leftwall

def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  stack.append((l, h))

  while stack:
    l, h = stack.pop()
    pivotIndex = partition(arr, l, h)

    if pivotIndex - 1 > l:
          stack.append((l, pivotIndex - 1))

    if pivotIndex + 1 < h:
        stack.append((pivotIndex + 1, h))

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)  

print("Sorted array is:", arr)


