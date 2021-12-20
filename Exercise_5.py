# Python program for implementation of Quicksort
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Did this code successfully run on Leetcode: Yes

# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot = arr[l]
  i, j = l, h
  while i <= j:
    while i < len(arr) and arr[i] <= pivot:
      i += 1
    while arr[j] > pivot:
      j -= 1
    if (i<j):
      arr[i], arr[j] = arr[j], arr[i]
  arr[l], arr[j] = arr[j], arr[l]
  return j

def quickSortIterative(arr, l, h):
  stack = [0] * (h-l+1)
  top = -1
  top += 1
  stack[top] = l
  top += 1
  stack[top] = h
  while top > -1:
    h = stack[top]
    top -= 1
    l = stack[top]
    top -= 1
    j = partition(arr, l, h)
    if l < j - 1:
      top += 1
      stack[top] = l
      top += 1
      stack[top] = j - 1
    if j + 1 < h:
      top += 1
      stack[top] = j + 1
      top += 1
      stack[top] = h

def printList(arr): 
  for i in range(len(arr)): 
    print (arr[i], end= " ")

if __name__ == '__main__': 
    arr = [4, 2, 6, 9, 2, 8, 1, 3]  
    print ("Given array is", end="\n")  
    printList(arr) 
    quickSortIterative(arr, 0, len(arr)-1)
    print("\n")
    print("Sorted array is: ", end="\n") 
    printList(arr)
