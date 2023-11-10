"""
Runtime Complexity:
1) O(n log n) where 'n' is the number of elements and the height of iterative stack goes log n levels.
- We initialise a stack, to add our sorted elements to. We choose a pivot and check if there are elements available to the left of pivot and add them the stack and same applies for the elements after pivot.
- Partition works same for both iterative and recursive method
-Yes, the code worked on leetcode
- To make sure my solution works, I created myself a driver program to check the loop invariant of the algorithm.
"""
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot =  arr[h]
    i = l-1
    for j in range(l,h):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[h] = arr[h], arr[i+1]
    return i+1
  #write your code here


def quickSortIterative(arr, l, h):
    size = h-l+1
    stack = [0]*(size)
    top = -1
    top = top+1
    stack[top] = l 
    top = top+1
    stack[top] =h
    
    
    while(top>=0):
        h = stack[top]
        top = top-1
        l = stack[top]
        top = top-1
        p = partition(arr,l,h)
        
        if p-1>l:
            top =top+1
            stack[top] = l
            top =top+1
            stack[top] = p-1
        if p+1<h:
            top = top+1
            stack[top] = p+1
            top = top+1
            stack[top] = h
        #write your code here
arr = [6,1,4,3,9,7]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
    print ("% d" % arr[i]),
