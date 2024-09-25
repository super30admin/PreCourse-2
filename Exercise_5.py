# Python program for implementation of Quicksort
''' Time complexity : O(n log n)
Space Complexity: O(log n)


Did this code successfully run on Leetcode : -
Any problem you faced while coding this : could not solve -> has to check geeks for geeks code.
Your code here along with comments explaining your approach '''

# This function is same in both iterative and recursive
def partition(arr, l, h): 
    i = ( l - 1 ) # index of smaller element
    x = arr[h] 
  
    for j in range(l, h): 
        if   arr[j] <= x: 
  
            # increment index of smaller element 
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i + 1], arr[h] = arr[h], arr[i + 1] 
    return (i + 1) 


# Function to do Quick sort 
def quickSortIterative(arr, l, h): 
  
    # Create a temp stack 
    size = h - l + 1
    stack = [0] * (size) 
  
    top = -1
  
    # push initial values of l and h to stack 
    top = top + 1
    stack[top] = l 
    top = top + 1
    stack[top] = h 
  
    # pop from stack
    while top >= 0: 
  
        # Pop h and l 
        h = stack[top] 
        top = top - 1
        l = stack[top] 
        top = top - 1
  
        # Set pivot element  
        p = partition( arr, l, h ) 
        # check for elements in left side of pivot and push to stack
        if p-1 > l: 
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = p - 1
  
        # check for elements in right side of pivot and push to stack
        if p + 1 < h: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
# Driver code to test above 
 

