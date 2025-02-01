# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    piv= arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<piv:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        arr[i+1], arr[h] = arr[h], arr[i+1]
        return i+1


def quickSortIterative(arr, l, h):
    stack = [0]*(h-1+1)
    top =-1
    top += 1
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