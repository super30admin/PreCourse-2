# Time Complexity : O(n log n) average, O(n²) worst case
# Space Complexity : O(log n) due to explicit stack
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : No, but remember to use explicit stack instead of recursion

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    # Choose rightmost element as pivot
    pivot = arr[h]
    
    # Index of smaller element (right position of pivot)
    i = l - 1
    
    # Iterate through all elements
    for j in range(l, h):
        # If current element is smaller than or equal to pivot, swap them
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in correct position
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quickSortIterative(arr, l, h):
    # Push initial values of l and h to stack
    stack = []
    stack.append(l)
    stack.append(h)
    
    # Keep popping from stack while it's not empty
    while stack:
        # Pop h and l
        h = stack.pop()
        l = stack.pop()
        
        pivot = partition(arr, l, h)
        
        # If there are elements on left side of pivot, push left side to stack
        if pivot - 1 > l:
            stack.append(l)
            stack.append(pivot - 1)
        
        # If there are elements on right side of pivot, push right side to stack
        if pivot + 1 < h:
            stack.append(pivot + 1)
            stack.append(h)

# Driver code to test the above code
if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSortIterative(arr, 0, n-1)
    print("Sorted array is:")
    for i in range(n):
        print(arr[i], end=" ")
    print()

