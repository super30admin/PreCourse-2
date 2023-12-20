# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
#TC = O(nlogn)
#SC = O(logn)

def partition(arr, low, high):
  #write your code here
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1

def quickSortIterative(arr, low, high):
  #write your code here
    stack = [0] * (high - low + 1)
    top = -1

    top += 1
    stack[top] = low
    top += 1
    stack[top] = high

    while top >= 0:
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1

        p = partition(arr, low, high)

        if p - 1 > low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = p - 1

        if p + 1 < high:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = high


arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  