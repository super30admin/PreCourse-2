# Python code to implement iterative Binary Search.

# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
    if r > l:
        mid = (l+(r - 1)) // 2
        if x == arr[mid]:
            return mid
        if x > arr[mid]:
            return binarySearch(arr, mid + 1, r, x)
        return binarySearch(arr, l, mid - 1, x)
    elif r == l:
        return r
    return -1


# Test array 
arr = [2, 3, 4, 10, 40]
x = 3

# Function call 
result = binarySearch(arr, 0, len(arr), x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
