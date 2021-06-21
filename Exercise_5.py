#Time Complexity :  O(nlogn)
#Space Complexity : O(1)
#Did this code successfully run on Leetcode : yes
#Any problem you faced while coding this : no

# Python program for implementation of Quicksort
from collections import deque
def partition(arr, l, h):
  # Initializing pivot's index 
    low=l
    high=h
    piv_index = low
    pivot = arr[piv_index]
    
    while low < high:
         
        # Increment the low pointer till it finds an element greater than  pivot
        while low < len(arr) and arr[low] <= pivot:
            low += 1
             
        # Decrement the high pointer till it finds an element less than pivot
        while arr[high] > pivot:
            high -= 1
   
        # swap the numbers on start and end if low and high not crossed each other
        if(low < high):
            arr[low], arr[high] = arr[high], arr[low]
     
    # Swap pivot element with element on high pointer
    arr[high], arr[piv_index] = arr[piv_index], arr[high]
    
    # Returning high when divided arr in two parts
    return high
  


def quickSortIterative(arr, l, h):
  # create a stack 
    stack = deque()
 
 
    # push the l and h index of the array into the stack
    stack.append((l, h))
 
    # loop till stack is empty
    while stack:
 
        l, h = stack.pop()
 
        # rearrange elements across pivot
        p = partition(arr, l, h)
 
        # push sublist indices containing elements that are less than the current pivot to stack
        if p - 1 > l:
            stack.append((l, p - 1))
 
        # push sublist indices containing elements that are more than the current pivot to stack
        if p + 1 < h:
            stack.append((p + 1, h))
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),