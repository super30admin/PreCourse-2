# Python program for implementation of Quicksort
# Approach - Similar to recursive but for iterative use a stack of (low, high)
# parition around the pivot and then push the new left and right ranges
# repeat this process until stack is empty.
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
  stack = [(l, h)]
  while stack:
      l, h = stack.pop()
      if l < h:
          pi = partition(arr, l, h)
          stack.append((l, pi - 1))
          stack.append((pi + 1, h))

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 

