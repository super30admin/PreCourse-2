# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):
    # array is assumed to be sorted in ascending order
    # check if end is greater than or equal to begin
    if r >= l:
        mid = (r+l)//2
        if arr[mid] == x:
            return mid
        # If the element at middle is less than x, then the element is in second half
        elif arr[mid] < x:
            return binarySearch(arr, mid+1, r, x)
        else:
        # If the element at middle is greater than x, then the element is in first half
            return binarySearch(arr, l, mid-1, x)
    return -1
    
# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")
