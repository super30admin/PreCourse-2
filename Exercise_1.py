# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Binary Search - Iterative Implementation
#keep adjusting the l and r pointers based on whether the middle value (mid) is smaller or greater than the target (x). 
#If found, return the index; if not, return -1.
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    
    return -1


# Test the binary search
arr = [2, 3, 4, 10, 40]
x = 10

result = binarySearch(arr, 0, len(arr) - 1, x)

# Output result
if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")
