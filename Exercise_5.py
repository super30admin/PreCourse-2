# Python program for implementation of Quicksort

# Time Complexity: O(n log n) average case, O(n^2) worst case
# Space Complexity: O(n)
# Did this code successfully run on Leetcode: Couldn't find this problem on Leetcode
# Any problem you faced while coding this: I need to practice more on this, it's a bit confusing

# This function is same in both iterative and recursive
def partition(arr, l, h):
    # Choose the rightmost element as pivot
    pivot = arr[h]
    
    # Pointer for greater element
    i = l - 1
    
    # Compare each element with pivot
    for j in range(l, h):
        if arr[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot element with the greater element specified by i
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    
    # Return the position from where partition is done
    return i + 1


def quickSortIterative(arr, l, h):
    # Create a stack
    stack = []
    
    # Push initial values
    stack.append((l, h))
    
    # Process stack until empty
    while stack:
        # Pop the top pair
        l, h = stack.pop()
        
        # Get pivot position
        p = partition(arr, l, h)
        
        # Push left subarray if it has more than one element
        if p - 1 > l:
            stack.append((l, p - 1))
        
        # Push right subarray if it has more than one element
        if p + 1 < h:
            stack.append((p + 1, h))

