# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
    pivot = arr[l]  
    i = l
    j = h
    while i < j:
        while i < h and arr[i] <= pivot:
            i += 1
        while j > l and arr[j] > pivot:  
            j -= 1
        if i < j:  
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[l], arr[j] = arr[j], arr[l]
    return j  

def quickSortIterative(arr, l, h):
  #write your code here
    size = h - l + 1
    stack = [0] * size  
    top = 0
    
    stack[top] = l
    top += 1
    stack[top] = h
    
    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1
        
        p = partition(arr, l, h)
        
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

# Test array
arr = [10, 80, 30, 90, 40, 50, 70]
quickSortIterative(arr, 0, len(arr) - 1)

print("Sorted array:")
for i in range(len(arr)):
    print(arr[i])
