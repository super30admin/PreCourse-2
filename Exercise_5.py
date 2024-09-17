# Python program for implementation of Quicksort

# This function is same in both iterative and recursive

def swap(arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr,low,high):
    pivot = arr[low]
    i = low 
    j = high
    while i < j:
        while  arr[i] <= pivot and i <= high - 1 :
            i += 1
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            swap(arr,i , j)

    swap(arr, low, j)
    return j


def quickSortIterative(arr, l, h):
    size = h - l + 1
    stack = [0] * 1000
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
        if l < h:
            p = partition(arr, l, h)
            if p - 1 > l:
                top = top + 1
                stack[top] = l
                top = top + 1
                stack[top] = p - 1
            if p + 1 < h:
                top = top + 1
                stack[top] = p + 1
                top = top + 1
                stack[top] = h

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:", arr)

    
  

