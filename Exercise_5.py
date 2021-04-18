
"""
Didn't know the solution for this, had to refer to online implementations,
for the idea of using an explicit stack.
"""

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr,low,high):
    i = low
    j = high
    pivot = arr[low]

    while i<j:
        #print(i,j,arr[i])
        while pivot >= arr[i] and i != len(arr) - 1 :
            #print(arr[i])
            i = i + 1
        while pivot <= arr[j] and j != 0 :
            j = j - 1
        if(i<j):
            arr[i],arr[j] = arr[j],arr[i]

    arr[low],arr[j] = arr[j],arr[low]

    return j


def quickSortIterative(arr, l, h):
  #write your code here
    size = h -l + 1
    stack = [0] * size

    top = -1
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h
    

    while top >= 0:

        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        p = partition(arr,l,h)
        if p - 1 > l:
           top += 1
           stack[top] = l
           top += 1
           stack[top] = p - 1

        if p + 1 < h:
              
           top += 1
           stack[top] = p + 1
           top += 1
           stack[top] = h


arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
            

        


