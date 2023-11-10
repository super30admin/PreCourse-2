""""// Time Complexity : 44ms
// Space Complexity : log(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach"""



# It returns location of x in given array arr if present, else returns -1
def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        middle = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[middle] == x:
            return middle

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[middle] > x:
            return binarySearch(arr, l, middle - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, middle + 1, r, x)

    else:
        # Element is not present in the array
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 11

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)
print(result)

if result != -1:
    print
    "Element is present at index % d" % result
else:
    print
    "Element is not present in array"