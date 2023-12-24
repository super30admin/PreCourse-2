# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l - 1

  for j in range(l, h):
      if arr[j] <= pivot:
          i += 1
          arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return i + 1


def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  stack.append((0, len(arr) - 1))

  while stack:
    l, h = stack.pop()

    # Partition the array and get the pivot index
    pivot_index = partition(arr, l, h)

    # If there are elements on the left side of the pivot, push them to the stack
    if pivot_index - 1 > l:
        stack.append((l, pivot_index - 1))

    # If there are elements on the right side of the pivot, push them to the stack
    if pivot_index + 1 < h:
        stack.append((pivot_index + 1, h))
        
    
    
#testing the algorithm

arr = [12, 4, 5, 6, 7, 3, 1, 15]
print("The array before sorting is ", arr)
quickSortIterative(arr, 0 , len(arr) - 1)
print("The array after sorting is", arr)


