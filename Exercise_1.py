# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):
    # write your code here
    '''
    Check if left<=right, if x == mid
    we found the element, else if
    x > arr[mid] then we need to move
    the left pointer to mid+1 and search
    the right side of the array.
    If x<arr[mid] we need to set right
    pointer to mid-1 and search left
    of the array.
    Time Complexity O(log(n))
    Space Complexity O(1)

    '''
    if len(arr) == 0:
        return -1

    while l <= r:
        mid = int ((l + r) / 2)
        if arr[mid] == x:
            return mid
            break
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return -1

def recBinarySearch(arr, l, r, x):

    if l <= r:
        mid = int ((l + r) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
            return recBinarySearch(arr,l,r,x)
        else:
            r = mid - 1
            return recBinarySearch(arr, l, r, x)
    return -1
# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = recBinarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
