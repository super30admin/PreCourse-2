# Time complexity - O(n log n)
# Space complexity - O(log n)
# Code runs properly

# Approach:
# Quick sort is divide and conquer algorithm.
# Using stack to simulate the recursive behavior, stack keeps track of the low and high index that needs sorting.
# Pop low and high to get range of elements being sorted from stack, apply partition, and push left and right subarray index back to the stack if they need further sorting.
# Where stack empty, array is fully sorted.


def partition(arr,low,high):
    pivot = arr[high]
    index = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            index+= 1
            arr[index], arr[j] = arr[j], arr[index]
    index+= 1        
    arr[index], arr[high] = arr[high], arr[index]
    return index

def quickSortIterative(arr, low , high):
    stack = []
    stack.append((low, high))
    
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = partition(arr, low, high)
            if pivot - 1 > low:
                stack.append((low, pivot - 1))
            if pivot + 1 < high:
                stack.append((pivot + 1, high))

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:", arr)
