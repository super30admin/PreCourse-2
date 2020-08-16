# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  divider = l
  pivot = h

  for i in range(l, h):
      if arr[i]<arr[pivot]:
          arr[i], arr[divider] = arr[divider], arr[i]
          divider+=1
      
  arr[pivot], arr[divider] = arr[divider], arr[pivot]
  
  return divider


def quickSortIterative(arr, l, h):
  #write your code here
  # Recursive method internally uses stack, so for iteravtive method the below code will be simulating the 
  # recursive method using stacks
  stack = [0]*(len(arr))
  top = -1
  top+=1
  stack[top] = l
  top+=1
  stack[top] = h

  while top>=0:
    h = stack[top]
    top-=1
    l = stack[top]
    top-=1

    x = partition(arr, l, h)

    if x-1>l:
      top+=1
      stack[top]=l
      top+=1
      stack[top]=x-1
    
    if x+1<h:
      top+=1
      stack[top]=x+1
      top+=1
      stack[top]=h
  
arr = [12, 34, 21, 4, 6, 12, 78] 
print("Array before sorting : ", arr)
quickSortIterative(arr, 0, len(arr)-1) 
print("Array after  sorting : ", arr)

