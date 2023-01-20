# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
# In each iteration we find the mid index of array and check if this number matches. 
# If yes we return else we check if the mid element obtained is lesser than x or greater than.
# If lesser than x we shrink array from mid element to end element, 
# if greater than we shrink array from strt of array to mid array element
# Time complexity - O(logn)
# Space complexity - O(1)
def binarySearch(arr, l, r, x):

    while l<=r:
        mid = (l+r)//2

        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            l = mid + 1
        else:
            r = mid - 1
    return -1



# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
