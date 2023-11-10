# Python program for implementation of Quicksort
# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot = arr[h]
  i = l - 1
  for j in range(l,h):
    if arr[j] < pivot:
      i = i+1
      #swap 
      arr[j], arr[i] = arr[i], arr[j]

  arr[i +1], arr[h] = arr[h], arr[i+1]
  return i + 1

  #write your code here


def quickSortIterative(arr, l, h):
  #create a temp stack
  arrLen = h - l + 1 
  stack = [0] * arrLen

  top = -1

  top  = top + 1
  stack[top] = l
  top = top + 1
  stack[top] = h

  #pop until not empty
  while top >=0:
    h = stack[top]
    top = top -1
    l = stack[top]
    top = top -1

    #sorted array
    p = partition(arr, l, h)

    # if elems on right side of pivot then push them to stack
    if p-1 > l:
      top  = top + 1
      stack[top] = l
      top = top +1
      stack[top] = p -1

    # if elems on right side of pivot then push them to stack
    if p +1 < h:
      top = top + 1
      stack[top] = p + 1
      top = top +1
      stack[top] = h

# Code to print the list 
def printList(arr): 
  for i in range(len(arr)):
    print(arr[i])  




arr = [10, 7, 8, 9, 1, 5]
print ("Given array is", end="\n")  
printList(arr) 
quickSortIterative(arr, 0, len(arr)-1) 
print("Sorted array is: ", end="\n") 
printList(arr) 