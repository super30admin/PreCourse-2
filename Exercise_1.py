# Python code to implement iterative Binary
# Search.
# Time Complexity: O(logN) where N is number of elements in the array
# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, low, high, x):

    # write your code here

    # base case
    if not arr:
        return -1

    while low < high:

        mid = low + (high - low) // 2  # Integer division

        if arr[mid] == x:
            # elemet found
            return mid

        if arr[mid] > x:
            # move left
            high = mid - 1

        if arr[mid] < x:
            # move right
            low = mid + 1

    # outside while loop
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
