#Time complexity: O(nlogn)
#Space Complexity: O(n)

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h): #create partition similar to recursive quicksort one
  #write your code here
  if len(arr) > 1:
    pivot = arr[h]
    i = l-1

    for j in range(l, h):
      if arr[j] <= pivot:
        i+=1
        arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[h], arr[h], arr[i+1]
    return i+1

def quickSortIterative(arr, l, h):
  #write your code here
  size = h-l+1 # here we initialise stack and store the low and high values in it
  stack = [0] *size
  top = -1

  top += 1
  stack[top] = l
  top += 1
  stack[top] = h
  
  while top >= 0: # until we have elements in stack we loop
    l = stack[top] # store the low and high values from the stack 
    top -= 1
    h = stack[top]
    top -= 1

    part = partition(arr, l, h) # call partititon for those elements

    if part-1 > l: # if the left side has more than 1 element we store the low and partititon-1 element in it
      top += 1
      stack[top] = l
      top += 1
      stack[top] = part -1
    
    if part + 1 < h: #we do the same process for right side 
      top += 1
      stack[top] = part + 1
      top += 1
      stack[top] = h
