# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
  #write your code here
    '''
     1. Consider the first element as pivot, pivot_index = 0
     2. Compare the pivot with the next element and set low to the index greater than pivot
     3. Start the iteration for the variable high. Continue the iteration till we get small element than pivot
     4. Swap the high and low and then swap the low element with pivot
    '''
    pivot_index = low
    pivot = arr[pivot_index]
    while low < high:
        #write your code here
        #Compare the pivot with the next element. Continue the iteration till we get the element greater than Pivot
        while low < len(arr) and arr[low] <= pivot:
            low = low + 1

        #Start the iteration for the variable high. Continue the iteration till we get small element than pivot
        while arr[high] > pivot:
            high = high - 1
        
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    
    arr[pivot_index], arr[low -1 ] = arr[low -1], arr[pivot_index]
    return low

def quickSortIterative(arr, low, high):
  #write your code here
  """
  1. First Declare the stack of size equal to array
  2. Push the low and high index to stack
  3. Pop those values and call the partition 
  4. Again perform the steps 2 and 3 for left and right elements of the Pivot element
  """
  top = -1
  stack = [0] * (high - low  + 1)
  
  #Push the values in the stack
  top = top + 1
  stack[top] = low
  top = top + 1
  stack[top] = high

  while top >= 0:
    #Pop the values from the stack
    high = stack[top]
    top = top - 1
    low = stack[top]
    top = top - 1

    partition_index = partition(arr,low, high)

    if partition_index - 1 > low:
      top = top + 1
      stack[top] = low
      top = top + 1
      stack[top] = partition_index -1
    
    if partition_index + 1 < high:
      top = top + 1
      stack[top] = partition_index + 1
      top = top + 1
      stack[top] = high


arr = [8, 7, 10, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print(f"Sorted array is: {arr}") 