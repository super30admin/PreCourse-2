def partition(arr,low,high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1] # move the pivot to its correct position
    return i+1


def quickSortIterative(arr, l, h):
    # simulate recursion with a stack
    stack = [(0,0)]*((h-l)//2)
    
    top = 0
    stack[0] = (l,h)

    while top>=0:
        l,h = stack[top] # pop
        top -= 1

        p = partition(arr,l,h)

        # instead of doing a recursive call
        # we push to the stack
        # with a check that the pivot is in bounds
        if p - 1 > l:
            stack[top] = (l,p-1)
            top += 1
        if p + 1 < h:
            stack[top] = (p+1, h)
            top += 1

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:", arr) 

