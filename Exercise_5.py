# approach:
#Create a function partition()-same as in recursion

#in quick sort,
#Pass three-parameters array, low, high
#Create Stack and initialize the top of the stack
#Push the initial value of low and high and keep popping it
#Set pivot element to its correct position
#Print the sorted array


# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot_index = l
  pivot = arr[pivot_index]
  while(l<h):
    while l < len(arr) and arr[l]<= pivot:
        l += 1
    while arr[h]> pivot:
        h -= 1
    if l < h:
        arr[l], arr[h] = arr[h], arr[l]
  arr[h], arr[pivot_index] = arr[pivot_index], arr[h]
  return h


def quickSortIterative(arr, l, h):
  #write your code here
  size = h - l + 1
  stack = [0] * (size)
  top = -1
  top += 1
  stack[top] = l
  top += 1
  stack[top] = h
 
    # Keep popping from stack while is not empty
  while top >= 0:
 
    # Pop high and low
    h = stack[top]
    top -= 1
    l = stack[top]
    top -= 1

    # sorted array
    p = partition( arr, l, h )

        # push left side to stack
    if p-1 > l:
      top = top + 1
      stack[top] = l
      top = top + 1
      stack[top] = p - 1

    #  push right side to stack
    if p+1 < h:
      top = top + 1
      stack[top] = p + 1
      top = top + 1
      stack[top] = h

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  

