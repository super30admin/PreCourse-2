# Time Complexity: O(log n) - each time, the search reduce by half, n/2 -> n/4 -> n/8 +...-> 1 => n/2 ^ k => log n
# Space Complexity: O(1)

# Python code to implement iterative Binary  
# Search. 
# Did this code successfully run on Leetcode : Yes (LeetCode 704)
# Any problem you faced while coding this : No

# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid -1

    return -1
        
  
# Test array 
arr = [2, 3, 4, 10, 40] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
assert binarySearch(arr, 0, len(arr)-1, 40) == 4
assert binarySearch(arr, 0, len(arr)-1, 4) == 2
assert binarySearch(arr, 0, len(arr)-1, 1) == -1
assert binarySearch(arr, 0, len(arr)-1, 50) == -1
assert binarySearch(arr, 0, len(arr)-1, 5) == -1
assert binarySearch(arr, 0, len(arr)-1, 2) == 0

arr = [7]
assert binarySearch(arr, 0, len(arr)-1, 7) == 0
assert binarySearch(arr, 0, len(arr)-1, 8) == -1

arr = []
assert binarySearch(arr, 0, len(arr)-1, 1) == -1

print("all tests pass")

if result != -1: 
    print(f"Element is present at index {result}")
else: 
    print("Element is not present in array")
