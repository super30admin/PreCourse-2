# Time Complexity: O(log n)

# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):

    while l <= r:
        mid = (l+r)//2

        if arr[mid] > x:  # if x is smaller than mid index, search left side of the tree
            return binarySearch(arr, l, mid-1, x)

        elif arr[mid] < x:  # if x is greater than mid index, search right side of the tree
            return binarySearch(arr, mid+1, r, x)

        else:  # if not in the right or left side of the tree then it is in the middle
            return mid
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
