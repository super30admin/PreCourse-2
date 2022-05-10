# Python program for implementation of Quicksort
#Time Complexity: O(NlogN)  first partition O(N) for every other partition (n/2) lesser lesser, so n times log2(n) 
#Space Complexity: O(N)  
# This function is same in both iterative and recursive
from Exercise_2 import quickSort


def partition(arr, l, h):
  #write your code here
    i = l - 1 
    x = arr[h]
 
    for j in range(l , h):
        if   arr[j] <= x:
 
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return i+1

def quickSortIterative(arr, l, h):
  #write your code here
    size = h - l + 1
    stack = [0] * (size)
 
    top = -1
 
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
 
    # Keep popping from stack while is not empty
    while top >= 0:
 
        # Pop high and low
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
 
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
arr = [10, 7, 13, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print (arr[i])