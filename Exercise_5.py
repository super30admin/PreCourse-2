# Python program for implementation of Quicksort

# Time Complexity:
# - Best Case: O(n log n) - When partitions are balanced (pivot divides array equally)
# - Average Case: O(n log n) - Expected performance over all possible inputs
# - Worst Case: O(n^2) - When partition is unbalanced (already sorted arrays with last element as pivot)

# Space Complexity:
# - O(log n) - We need stack space for storing start and end indices
# - This is better than O(log n) recursive stack space in standard Quicksort implementation

# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot = arr[h]  # Choose the rightmost element as pivot
  i = l - 1  # Index of smaller element
  
  for j in range(l, h):
      # If current element is smaller than or equal to pivot
      if arr[j] <= pivot:
          i += 1
          arr[i], arr[j] = arr[j], arr[i]
  
  # Place pivot at its correct position
  arr[i+1], arr[h] = arr[h], arr[i+1]
  return i+1


def quickSortIterative(arr, l, h):
   #Create an auxiliary stack
    size = h - l + 1
    stack = [0] * size
    
    # Initialize top of stack
    top = -1
    
    # Push initial values of l and h to stack
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h
    
    # Keep popping from stack while it's not empty
    while top >= 0:
        # Pop h and l
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1
        
        # Set pivot element at its correct position
        p = partition(arr, l, h)
        
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1
            
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h


# Driver code
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    
    print("Original array:")
    for i in range(n):
        print("%d" % arr[i], end=" ")
    print()
    
    # Call the quickSortIterative function
    quickSortIterative(arr, 0, n-1)
    
    print("Sorted array:")
    for i in range(n):
        print("%d" % arr[i], end=" ")
    print()