# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  pindex = l
  for i in range(l, h):
      if arr[i] <= pivot:
          arr[i], arr[pindex] = arr[pindex], arr[i]
          pindex += 1
  arr[pindex], arr[h] = arr[h], arr[pindex]
  return pindex

def quickSortIterative(arr, l, h):
  #write your code here
    size = h - l + 1
    stack = [0] * (size)
    top = -1
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h
    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1
        p = partition(arr, l, h)
        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1
        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print(arr[i])