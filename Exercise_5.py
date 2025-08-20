#Time complexity - Best and Avg case - O(n log n) Worst case - O(n²)
#Space complexity - Best  O(n log n) Worst case - O(n)

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l - 1
  for j in range(l, h):
    if arr[j] <= pivot:
      i = i+1
      arr[i], arr[j] = arr[j], arr[i]  #swap elements
  arr[i+1], arr[h] = arr[h], arr[i+1]  #swap pivot
  return i+1


def quickSortIterative(arr, l, h):
  #write your code here
  #use stack to remove recursion
  stack = [(l, h)]
  while stack:
    l, h = stack.pop()
    if l < h:
      pi = partition(arr, l, h)
      stack.append((l, pi-1))
      stack.append((pi+1, h))


arr = [10,7,8,9,1,5]
n = len(arr)
print("Original array:", arr)
quickSortIterative(arr, 0, n-1)
print("Sorted array:", arr)
