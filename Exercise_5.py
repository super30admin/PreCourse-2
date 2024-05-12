# Time complexity:  O(nlogn)
# space complexity: O(n)
 
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
  
    # assign first element of array as pivot
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        # traverce array from left to right 
        # increase i until you find element greater than pivot
        while arr[i] <= pivot and i < high:
            i += 1

        # traverce array from right to left 
        # decrease j until you find element greater than pivot   
        while arr[j] > pivot and j >= low:
            j -= 1
        
        # If i and j did not cross then swap elements 
        if i < j:
            (arr[i], arr[j]) = (arr[j], arr[i])
    
    # If i and j crossed each other we found sorted position for pivot
    # swap pivot with partitioning location 
    (arr[low], arr[j]) = (arr[j], arr[low])

    # retun partitioning position
    return j

def quickSortIterative(arr, low, high):
  #write your code here

  # Create an auxiliary stack
    size = high - low + 1
    stack = [0] * (size)
 
    # initialize top of stack
    top = -1
 
    # push initial values of l and h to stack
    top += 1
    stack[top] = low
    top += 1
    stack[top] = high
 
    # Keep popping from stack while is not empty
    while top >= 0:
 
        # Pop h and l
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1
 
        # Set pivot element at its correct position in
        # sorted array
        p = partition( arr, low, high )
 
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = p - 1
 
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p+1 < high:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = high


# Code to print the list 
def printList(arr): 
    
    #write your code here
  for i in arr:
    print ("%d" %i)
    
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [10, 7, 8, 9, 1, 5] 
    print ("Given array is", end="\n")  
    printList(arr) 
    n = len(arr)
    quickSortIterative(arr, 0, n-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
