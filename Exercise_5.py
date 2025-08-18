# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    """
    Partition function using Lomuto partition scheme.
    Takes last element as pivot, places the pivot element at its correct
    position in sorted array, and places all smaller elements to left
    of pivot and all greater elements to right of pivot.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Choose the rightmost element as pivot
    pivot = arr[h]
    
    # Index of smaller element indicates the right position of pivot found so far
    i = l - 1
    
    for j in range(l, h):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1  # increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # swap elements
    
    # Place pivot at correct position
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1  # return position of pivot


def quickSortIterative(arr, l, h):
    """
    Iterative implementation of QuickSort using only a stack.
    
    Time Complexity: 
    - Best/Average Case: O(n log n)
    - Worst Case: O(n²)
    Space Complexity: O(log n) for stack space
    """
    # Create a stack to store pairs of (low, high) indices
    stack = []
    
    # Push initial values of l and h to stack as a tuple
    stack.append((l, h))
    
    # Keep processing while stack is not empty
    while stack:
        # Pop low and high indices from stack
        low, high = stack.pop()
        
        # Only process if there are at least 2 elements
        if low < high:
            # Partition the array and get pivot index
            pivot_index = partition(arr, low, high)
            
            # Push left subarray to stack (if it has more than 1 element)
            if pivot_index - 1 > low:
                stack.append((low, pivot_index - 1))
            
            # Push right subarray to stack (if it has more than 1 element)
            if pivot_index + 1 < high:
                stack.append((pivot_index + 1, high))


def quickSortRecursive(arr, l, h):
    """
    Recursive implementation of QuickSort.
    
    Time Complexity: 
    - Best/Average Case: O(n log n)
    - Worst Case: O(n²)
    Space Complexity: O(log n) for recursion stack
    """
    if l < h:
        # Partition the array and get pivot index
        pi = partition(arr, l, h)
        
        # Recursively sort elements before and after partition
        quickSortRecursive(arr, l, pi - 1)
        quickSortRecursive(arr, pi + 1, h)


def print_array(arr):
    """Helper function to print array"""
    print(" ".join(map(str, arr)))


# Test the implementation
if __name__ == "__main__":
    # Test case 1: Random array
    print("=== QuickSort Implementation Test ===")
    
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {arr1}")
    
    # Test iterative quicksort
    arr1_copy = arr1.copy()
    quickSortIterative(arr1_copy, 0, len(arr1_copy) - 1)
    print(f"Sorted (Iterative): {arr1_copy}")
    
    # Test recursive quicksort
    arr1_copy2 = arr1.copy()
    quickSortRecursive(arr1_copy2, 0, len(arr1_copy2) - 1)
    print(f"Sorted (Recursive): {arr1_copy2}")
    
    print()
    
    # Test case 2: Already sorted array
    arr2 = [1, 2, 3, 4, 5]
    print(f"Already sorted array: {arr2}")
    arr2_copy = arr2.copy()
    quickSortIterative(arr2_copy, 0, len(arr2_copy) - 1)
    print(f"After quicksort: {arr2_copy}")
    
    print()
    
    # Test case 3: Reverse sorted array
    arr3 = [5, 4, 3, 2, 1]
    print(f"Reverse sorted array: {arr3}")
    arr3_copy = arr3.copy()
    quickSortRecursive(arr3_copy, 0, len(arr3_copy) - 1)
    print(f"After quicksort: {arr3_copy}")
    
    print()
    
    # Test case 4: Array with duplicates
    arr4 = [3, 6, 8, 10, 1, 2, 1]
    print(f"Array with duplicates: {arr4}")
    arr4_copy = arr4.copy()
    quickSortIterative(arr4_copy, 0, len(arr4_copy) - 1)
    print(f"After quicksort: {arr4_copy}")
    
    print()
    
    # Test case 5: Single element
    arr5 = [42]
    print(f"Single element array: {arr5}")
    arr5_copy = arr5.copy()
    quickSortRecursive(arr5_copy, 0, len(arr5_copy) - 1)
    print(f"After quicksort: {arr5_copy}")
    
    print()
    
    # Test case 6: Empty array
    arr6 = []
    print(f"Empty array: {arr6}")
    if arr6:  # Only sort if array is not empty
        quickSortIterative(arr6, 0, len(arr6) - 1)
    print(f"After quicksort: {arr6}")
