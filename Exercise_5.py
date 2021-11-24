# Time complexity = o(nlog(n))
#space complexity: O(n)
# Python program for implementation of Quicksort
# iterative quick sort follows the same technique as divide and concure. This question made me to think the right approach and is willing to learn more in class.

# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot = arr[h]
  small = (l - 1)

  for i in range(l, h):
    if arr[i] <= pivot:
      small += 1
      arr[small], arr[i] = arr[i], arr[small]
  arr[small + 1], arr[h] = arr[h], arr[small + 1]
  return(small + 1)



def quickSortIterative(arr, l, h):
  if l < h:
    part = partition(arr, l, h)

    quickSortIterative(arr, l, part-1)
    quickSortIterative(arr, part + 1, h)

