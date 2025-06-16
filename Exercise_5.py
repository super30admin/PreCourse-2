# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    #write your code here
    pivot = arr[h]
    i = l - 1

    for j in range(l, h):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i+1

def quickSortIterative(arr, l, h):
    
    #write your code here
    stack = []

    stack.append((l,h))

    while stack:
        low, high = stack.pop()

        if low < high:
            
            pivotIndex = partition(arr, low, high)

            stack.append((low, pivotIndex - 1))
            stack.append((pivotIndex+1, high))

    return arr


