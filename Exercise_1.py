# Time Complexity: O(log n): search window halves every iteration
# Space Complexity: O(1):only a fixed number of variables used
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

def binarySearch(arr, l, r, x):
    low = l                          # start of search window, passed in as l
    high = r                         # end of search window, passed in as r

    while low <= high:               # keep searching while window is valid
        mid = (low + high) // 2      # find middle index using integer division

        if arr[mid] == x:            # found the target at mid
            return mid               # return the index

        elif arr[mid] < x:           # target is larger, so it's in the right half
            low = mid + 1            # shrink left boundary

        else:                        # target is smaller, so it's in the left half
            high = mid - 1           # shrink right boundary

    return -1                        # target not found in array


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", result)  
else:
    print("Element is not present in array")       