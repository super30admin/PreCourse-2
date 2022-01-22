# Python program for implementation of Quicksort 
# // Time Complexity : O(nlogn) for best and avg and O(n^2) for worst case
# // Space Complexity : O(logn)
  
# This function is same in both iterative and recursive
def partition(arr,l,h):
    i = ( l - 1 )
    x = arr[h]
  
    for j in range(l , h):
        if   arr[j] <= x:
  
           
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
  
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)
  

def quickSortIterative(arr,l,h):
  
   
    n = h - l + 1
    stack = [0] * (n)
  
    
    top = -1
  
    
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
  
    while top >= 0:
  
        
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
  
        
        p = partition( arr, l, h )
  
        
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
  
        
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
  

arr = [10,23,7,4,34,13]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),