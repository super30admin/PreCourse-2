#Time Complexity  O(n^2) and space complexity O(n)
# Python program for implementation of Quicksort



# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l-1

  for j in range(l,h):
    if arr[j] <= pivot:
      i+=1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[h] = arr[h], arr[i+1]
  return i+1


def quickSortIterative(arr, l, h):
  #write your code here
    stack = []

    stack.append((1, h))

    while stack:
      l,h = stack.pop()

      if l<h:
        pivot = partition(arr, l, h)
        stack.append((l, pivot - 1))
        stack.append((pivot + 1, h))