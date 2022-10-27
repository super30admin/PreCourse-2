# Python program for implementation of Quicksort
# This function is same in both iterative and recursive
#Time Complexity: O(n^2)
#Space Complexity: O(n)
def partition(arr, l, h):
  pElem = arr[h]
  pIndex = l
  
  for curIndex in range(l, h):
    curElem = arr[curIndex]
    if curElem <= pElem:
      swap(arr, pIndex, curIndex)
      pIndex += 1
  
  swap(arr, pIndex, h)
  return pIndex


def swap(arr, i1, i2):
  temp = arr[i1]
  arr[i1] = arr[i2]
  arr[i2] = temp


def quickSortIterative(arr, l, h):
  stack = [[l,h]]

  while len(stack):
    curStackTop = stack.pop()
    start, end = curStackTop[0], curStackTop[1]
    if start < end:
      pIndex = partition(arr, start, end)
      stack.append([pIndex+1, end])
      stack.append([start, pIndex-1])

if __name__ == '__main__':
  a = [29, 36, 14, 88, 22, 9, 13, 12, 2]
  quickSortIterative(a, 0, 8)
  print(f'sorted {a}')




