# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  i = (l - 1)        
  pivot = arr[h]
  for j in range(l, h):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return (i + 1)


def quickSortIterative(arr, l, h):
  if l < h:
    pi = partition(arr, l, h)
    quickSortIterative(arr, l, pi-1)
    quickSortIterative(arr, pi + 1, h)

if __name__ == '__main__' :
     
    arr = [4, 2, 5, 3, 1]
    n = len(arr)
     
    # Calling quickSort function
    quickSortIterative(arr, 0, n - 1)
     
    for i in range(n):
        print(arr[i], end = " ")

