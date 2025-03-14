# Python program for implementation of Quicksort
# Time Complexity : O(n^2)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : online GDB compiler
# Any problem you faced while coding this : NO 

# This function is same in both iterative and recursive
# This function partitions the array and returns the pivot index.
def partition(arr, low, high):
    pivot = arr[high]         # Choose the pivot as the last element
    i = low - 1               # i will track the index for smaller elements
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements to move smaller ones left
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in the correct position
    return i + 1

# Iterative QuickSort function using a list as a stack
def quickSortIterative(arr, low, high):
    # Create an empty list to use as a stack
    stack = []
    
    # Push the initial range (low and high) onto the stack
    stack.append((low, high))
    
    # Continue until there are no more sub-arrays to sort
    while stack:
        # Pop the current range from the stack
        low, high = stack.pop()
        
        # Partition the sub-array and get the pivot index
        p = partition(arr, low, high)
        
        # If there are elements on the left of the pivot, push that range onto the stack
        if p - 1 > low:
            stack.append((low, p - 1))
            
        # If there are elements on the right of the pivot, push that range onto the stack
        if p + 1 < high:
            stack.append((p + 1, high))

# Example usage:
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    quickSortIterative(arr, 0, len(arr) - 1)
    print("Sorted array is:")
    print(arr)