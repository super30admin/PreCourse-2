'''
Time Complexity : O(n^2) worst Case
Space Complexity : O(LogN)

'''
def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quickSortIterative(arr,l,h):
    top = -1
    size = h - l + 1
    stack = [0] * (size)
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
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
