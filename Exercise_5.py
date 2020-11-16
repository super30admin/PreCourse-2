# Python program for implementation of Quicksort

# This function is same in both iterative and recursive

#Taking Last element as pivot element
# Elements smaller than pivot on comparison with current will be stored left of pivot
# and greater than on the right of pivot

def partition(arr, low, high): 
    i = ( low - 1 ) 
    x = arr[high] 
  
    for j in range(low, high): 
        if   arr[j] <= x: 

            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    return (i + 1) 
  
# An explict/auxiliary stack is maintained which stores starting and ending indices
# of the array on which quicksort is performed
def quickSortIterative(arr, low, high): 
  
    size = high - low + 1
    stack = [0] * (size) 
  
    # initializing the top of stack 
    top = -1
  
    # pushing initial values of low and high to stack 
    top = top + 1
    stack[top] = low 
    top = top + 1
    stack[top] = high 
  
    #  # Popping high and low from stack while is not empty 
    while top >= 0: 
        high = stack[top] 
        top = top - 1
        low = stack[top] 
        top = top - 1
        pivot_element = partition( arr, low, high ) 
  
        # If there are elements on left side of pivot, 
        # then pushing left side to stack 
        if pivot_element-1 > low: 
            top = top + 1
            stack[top] = low 
            top = top + 1
            stack[top] = pivot_element - 1
  
        # If there are elements on right side of pivot, 
        # then pushing right side to stack 
        if pivot_element + 1 < high: 
            top = top + 1
            stack[top] = pivot_element + 1
            top = top + 1
            stack[top] = high 

# Driver code to test above 
arr = [4, 3, 5, 2, 1, 3, 2, 3] 
n = len(arr) 
quickSortIterative(arr, 0, n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("% d" % arr[i]), 