# Python program for implementation of Quicksort
# Time Complexity: O(nlogn)
# Space Complexity: O(n)

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[l]
  i = l + 1
  j = h
  while True:
      while i <= j and arr[i] <= pivot:
          i += 1
      while i <= j and arr[j] > pivot:
          j -= 1
      if i <= j:
          arr[i], arr[j] = arr[j], arr[i]
      else:
          break
  arr[l], arr[j] = arr[j], arr[l]
  return j


def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  stack.append((0, len(arr) - 1))  # Initial range to sort

  while stack:
      l, h = stack.pop()
      pivot_idx = partition(arr, l, h)

      if pivot_idx - 1 > l:
          stack.append((l, pivot_idx - 1))
      if pivot_idx + 1 < h:
          stack.append((pivot_idx + 1, h))


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 

