# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
  #write your code here
  i = low - 1
  for j in range(low, high):
      if arr[j] < arr[high]:
          i += 1
          arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1


def quickSortIterative(arr, l, h):
    stack = []
    stack.append(l)
    stack.append(h)
    while stack:
        h = stack.pop()
        l = stack.pop()
        pindex = partition(arr, l, h)
        if pindex-1 > l:
            stack.append(l)
            stack.append(pindex-1)
        elif pindex+1 < h:
            stack.append(pindex + 1)
            stack.append(h)


  #write your code here

