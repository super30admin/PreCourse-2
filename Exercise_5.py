# Python program for implementation of Quicksort
# This function is same in both iterative and recursive
#time complexity: O(n*log(n)
#space complexity: O(n)

def partition(arr, l, h):
  swap = l                                       #taking swap position and pivot position as the leftmost
  for i in range(l+1, h+1):
    if arr[i] < arr[l]:                          #finding the smaller element and swaping it with pivot till pivot reaches partition position
      swap+=1
      (arr[i],arr[swap]) = (arr[swap],arr[i])
  (arr[l],arr[swap]) = (arr[swap], arr[l])      #swap pivot with the smaller element
  return swap

def quickSortIterative(arr, l, h):
  size = h-l+1
  stack = [0]*(size)   #create an auxiliary stack
  top = -1             #initialise top
  
  top = top + 1
  stack[top] = l
  top = top + 1
  stack[top] = h       #push initial values of l & h to stack

  while top >= 0:
    h=stack[top]
    top=top-1
    l=stack[top]
    top=top-1            #pop h and l

    p = partition(arr,l,h)   #set pivot to its position
    if p - 1 > l:             #if elements on left side of pivot then push left side to stack
        top = top + 1
        stack[top] = l
        top = top + 1
        stack[top] = p - 1
    if p + 1 < h:            #if elements on right side of pivot then push right side to stack
        top = top + 1
        stack[top] = p + 1
        top = top + 1
        stack[top] = h
  return arr


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
sorted_arr = quickSortIterative(arr, 0, n - 1)
print(f"Sorted array is: {sorted_arr}")
    
    
  
  

