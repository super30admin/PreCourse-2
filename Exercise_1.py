# Python code to implement iterative Binary Search.# It returns location of x in given array arr if present, else returns -1
# Time Complexity = O(logn)
# Space Complexity = O(1)

def binarySearch(arr, l, r, x):

    while l<=r:
        mid = l + (r-l) // 2 #finding pivot index

        if arr[mid] == x: #if pivot element is itself target
            return mid

        if x < arr[mid]: #if target is less than pivot element, search in left half
            r = mid -1
        else:
            l = mid + 1 #if target is greater than pivot element, search in right half

    return -1 # if target does not exist at all




# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
