# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
# Time Complexity : O(logn)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Implemented it in vs code
# Any problem you faced while coding this : No


def binarySearch(arr, l, r, x):

    while l <= r:
        # middle value
        mid = l + ((r-l)//2)
        #  if x is the middle element
        if arr[mid] == x:
            return mid
        # if x > than middle element, then x probably lies in the right side of the array
        elif x > arr[mid]:
            l = mid + 1
        #  else x probably lies in the left side of the array
        else:
            r = mid - 1
    #  if the return in line 19 dint execute, then the element does not exist in the array
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
