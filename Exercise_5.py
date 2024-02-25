# Python program for implementation of iterative Quicksort
# Time Complexity : O(nlogn)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Yes, this is the one I had most trouble with.

# This function is same in both iterative and recursive

def partition(arr,l, h):
    #write your code here
    pivot = arr[l]
    #Selects the pivot and two pointers
    i = l
    j = h
    
    #Loop runs till i & j cross each other
    while (i < j):
        while (arr[i] <= pivot and i <= h - 1):
            i += 1
        while (arr[j] > pivot and j >= l + 1):
            j -= 1
        
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]

    #Once done, swap the pivot with j to it's position      
    arr[l], arr[j] = arr[j], arr[l]
    return j


def quickSortIterative(arr, l, h):
  #write your code here
    #Creates a stack based on the length of the array
    size = h - l + 1
    stack = [0] * size
    
    #top of the stack
    top = -1
    
    #pushes the lowest and highest values to the stack
    top = top + 1
    stack[top] = l
    top = top + 1 
    stack[top] = h
    
    #runs till the stack is not empty
    while top>=0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1 
        
        #set the postion for pivot
        p = partition(arr, l , h)
        
        #elements from left side of pivot are pushed to stack
        if p-1 > l: 
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = p - 1

        #elements from right side of pivot are pushed to stack
        if p + 1 < h: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h 

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  
