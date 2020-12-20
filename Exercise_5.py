# -*- coding: utf-8 -*-
"""
Python Implementation of Iterative Quicksort

Complexity : O(nlon) where n is the length of array
"""
# This function is same in both iterative and recursive
def partition(arr,l,h): 
    i = (l-1)         # smallest element stored in i 
    pivot = arr[h]     #pivot holds the largest element in the array
  
    for j in range(l,h): # run though the entire array (from low to high)
  
        # If current element is smaller than the pivot 
        if arr[j]<pivot: 
                   
            i = i+1 #move to the next element in the array till pivot position
            arr[i],arr[j] = arr[j],arr[i] #swap the consecutive elements
  
    arr[i+1],arr[h] = arr[h],arr[i+1] #swap the next element in the array with the largest 
    return (i+1) #return the index of partitioned element
  

def quickSortIterative(arr, l, h):
    #in itertaive quicksort, we implement the sorting using stack DS 
    
    size = h - l + 1 #initialize size of stack to be length of array
    stack = [0] * (size) 
  
    top = -1 #Initialize the stack index
  
    # push initial values of l and h to stack 
    top = top + 1
    stack[top] = l #start with leftmost elem
    top = top + 1
    stack[top] = h 
  
    #pop from stack
    while top >= 0: 
  
        # Pop h and l 
        h = stack[top] 
        top = top - 1
        l = stack[top] 
        top = top - 1
  
        p = partition(arr,l,h) #gets the index of the pivotted element
  
        #if elements are on left of pivotted elemnt, push them onto the stack
        if p-1 > l: 
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = p - 1
  
        #if elements are on right side of pivotted elem, push them onto stack
        if p + 1 < h: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h 
  
# Driver code to test above 
arr = [4, 3, 5, 2, 1, 3, 2] 
n = len(arr) 
quickSortIterative(arr, 0, n-1) 
print ("Sorted array is:") 
for i in range(n): print (arr[i]) 
  