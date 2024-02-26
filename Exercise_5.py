# Python program for implementation of Quicksort
# Time complexity is O(NLogN) and space complexity is O(N)
# This function is same in both iterative and recursive
def partition(arr, low, high):
    # select pivot as highest element
    pi = arr[high]
    # assign lower value index
    i = low-1
    for j in range(low, high):
        # if the element is smaller than the pivot swap with the greater element pointed by i
        if arr[j] <= pi:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]   
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1  

def quickSortIterative(arr, low, high):

  #  auxiliary stack
  size = high - low + 1
  stack = [0] * (size)

  top = -1

  top = top + 1
  stack[top] = low
  top = top + 1
  stack[top] = high

  # Keep popping from stack while is not empty
  while top >= 0:

    # Pop high and low
    high = stack[top]
    top = top - 1
    low = stack[top]
    top = top - 1

    # sorted array
    p = partition( array, low, high )

    # push left side to stack
    if p-1 > low:
        top = top + 1
        stack[top] = low
        top = top + 1
        stack[top] = p - 1

    #  push right side to stack
    if p+1 < high:
        top = top + 1
        stack[top] = p + 1
        top = top + 1
        stack[top] = high
 
array = [9, 0, 8, 1, 7, 3, 6, 4]
n = len(array)
print("Orignal Array:", array)
quickSortIterative(array, 0, n-1)
print ("Sorted Array :", array)
