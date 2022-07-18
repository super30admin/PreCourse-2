"""
Exercise_5 : Iterative Quick Sort.
Time Complexity : 
    Best case: O(nlogn)
    Worst Case: O(N^2)

Space Complexity : O(1) 


@name: Rahul Govindkumar_RN27JUL2022
"""

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr,low,high):
    #write your code here
    
    #Pivot as First element
    pivot = arr[low]
    
    i=low
    j= high
    
    #loop untill the pointers cross each other 
    while i < j :
        
        #to find the ith position untill the value is less than the pivot
        while  i <= j and (arr[i] <= pivot)  :
            i +=1
        
        #to find the ith position untill the value is greater than the pivot
        while i <= j and (arr[j] > pivot) :
            j -=1
        
        #Swap ith position and jth position value  if they havent crossed each other   
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
            
        else:
            break
    
            #Swap the pivot value with the jth value
    arr[low], arr[j] = arr[j], arr[low]
    
    return j


def quickSortIterative(arr, left, right):
    #write your code here
    
    #Initializing Stack and top 
    size = right - left + 1
    stack = [0] * (size)
    
    top = -1
    
    # Adding initial values of left and right to stack
    top = top + 1
    
    stack[top] = left
    top = top + 1
    
    stack[top] = right
    
    # Lopp until stack is not empty
    while top >= 0:
        
        # Pop right and left
        right = stack[top]
        top = top - 1
        left = stack[top]
        top = top - 1
        
        
        p = partition( arr, left, right )
        
        # If there are elements on left side of pivot,
        # Push left side to stack
        if p-1 > left:
            top = top + 1
            stack[top] = left
            top = top + 1
            stack[top] = p - 1
            
        # If there are elements on right side of pivot,
        # Push right side to stack
        if p + 1 < right:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = right

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
print ("Array befor Sorting:") 
for i in range(n): 
    print ("%d" %arr[i], end=" "), 
    
quickSortIterative(arr,0,n-1) 

print ("\n\nSorted array is:") 
for i in range(n): 
    print ("%d" %arr[i], end=" "), 
  
 
