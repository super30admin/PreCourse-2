""" 
Exercise_1 : Binary Search. (Iterative Solution)

# Time Complexity :
- O(log n) where n is the size of array (each iteration reduces search space by half)
  - Base 2 log due to binary splitting

# Space Complexity :
- O(1) (only using constant extra space for variables l, r, m)

"""

def binarySearch(arr, l, r, x):
    while l <= r:  
        m = (l + r) // 2
        
        # If element found at mid, return index
        if arr[m] == x:
            return m
        
        # If element is larger than mid, ignore left half else ignore right half
        if arr[m] > x:
            r = m - 1
        else:
            l = m + 1

    return -1
    
# Test array 
arr = [2, 3, 4, 10, 40]  # Must be sorted for binary search
  
# Test cases for elements in array
assert binarySearch(arr, 0, len(arr)-1, 2) == 0
assert binarySearch(arr, 0, len(arr)-1, 3) == 1
assert binarySearch(arr, 0, len(arr)-1, 4) == 2
assert binarySearch(arr, 0, len(arr)-1, 10) == 3
assert binarySearch(arr, 0, len(arr)-1, 40) == 4

# Test cases for elements not in array
assert binarySearch(arr, 0, len(arr)-1, 1) == -1
assert binarySearch(arr, 0, len(arr)-1, 50) == -1

print("All tests passed")