# Time Complexity : O(nlogn) as it is divide and conquer, and we divide the list(which is logN ) n times
# Space Complexity : O(N) for the stack
# Did this code successfully run on Leetcode : I did not find this exact question on leetcode
# Any problem you faced while coding this : No problem faced as such, it strengthened my understanding of quicksort


# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):

  low = l - 1
  pivot = arr[h]
  for i in range(l, h):
    if arr[i] <= pivot:
      low += 1
      arr[low], arr[i] = arr[i], arr[low]
  arr[low + 1], arr[h] = arr[h], arr[low + 1]
  return (low + 1)


def quickSortIterative(arr, l, h):
  #write your code here

  # Create a stack
  size = h - l + 1
  stack  = [0] * size

  # top of stack
  top = -1

  # push intial l and h on the stack
  top += 1
  stack[top] = l
  top += 1
  stack[top] = h

  while top >= 0:

    # pop l and h from stack
    h = stack[top]
    top -= 1
    l = stack[top]
    top -= 1

    # get the pivot element
    pivot = partition(arr, l, h)

    # if there are elements to the left of pivot, push them on to the stack
    # do not include the pivot element, so (pivot - 1)
    if (pivot - 1) > l:
      top += 1
      stack[top] = l
      top += 1
      stack[top] = pivot - 1

    # if there are elements to the right of pivot, push them onto the stack
    # do not include the pivot element, so (pivot + 1)
    if pivot + 1 < h:
      top += 1
      stack[top] = pivot + 1
      top += 1
      stack[top] = h

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
print ("\nUnsorted array is:") 
for i in range(n): 
  print (arr[i], end=' ')
print()
quickSortIterative(arr,0,n-1) 
print ("\nSorted array is:") 
for i in range(n): 
  print (arr[i], end=' ')
print('\n')
  