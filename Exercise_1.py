'''2 Approaches'''
'''
binarySearch:
  Recursive Approach
    Space Complexity: O(logn) as the nested function calls will create a call stack
  Iterative Approach
    Space Complexity: O(1) as we always need constant space for left right and mid pointers

  Iterative Approach and Recursive Approach
    Sorted Time Complexity: O(log n) as we halve the array and search at every iteration
    Unsorted Time Complexity: O(n log n) as we have to sort the array first and then we can search

'''
# Python code to implement iterative Binary Search.
# It returns location of x in given array arr
# if present, else returns -1

print("Iterative Binary Search")


def binarySearch(arr, l, r, x, sorted=False):
    # write your code here
    if not sorted:
        arr.sort()
    left = l
    right = r
    while left <= right:
        mid = (left + right) // 2
        # Search right half
        if arr[mid] < x:
            left = mid + 1
        # Search left half
        elif arr[mid] > x:
            right = mid - 1
        # Element Found
        else:
            return mid
    # Element not found
    return -1


# Default Test Case
# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x, True)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")

# ######################Additional Test Cases##########################
# (1) Sorted Array
arr = [2, 3, 4, 10, 40]
op = binarySearch(arr, 0, len(arr)-1, 2, True)
assert op == 0, f"Expected 0 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 3, True)
assert op == 1, f"Expected 1 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 4, True)
assert op == 2, f"Expected 2 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 10, True)
assert op == 3, f"Expected 3 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 40, True)
assert op == 4, f"Expected 4 as output but instead got {op}"

op = binarySearch(arr, 0, len(arr)-1, 0, True)
assert op == -1, f"Expected -1 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 5, True)
assert op == -1, f"Expected -1 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 100, True)
assert op == -1, f"Expected -1 as output but instead got {op}"

# (1) UnSorted Array
arr = [2, 40, 4, 3, 10]
op = binarySearch(arr, 0, len(arr)-1, 2)
assert op == 0, f"Expected 0 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 3)
assert op == 1, f"Expected 1 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 4)
assert op == 2, f"Expected 2 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 10)
assert op == 3, f"Expected 3 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 40)
assert op == 4, f"Expected 4 as output but instead got {op}"

op = binarySearch(arr, 0, len(arr)-1, 0)
assert op == -1, f"Expected -1 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 5)
assert op == -1, f"Expected -1 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 100)
assert op == -1, f"Expected -1 as output but instead got {op}"
# #######################################################################

# Python code to implement recursive Binary Search.
# It returns location of x in given array arr
# if present, else returns -1
print("Recursive Binary Search")


def binarySearch(arr, l, r, x, sorted=False):
    # write your code here
    if not sorted:
        arr.sort()

    mid = (l + r) // 2
    if l <= r:
        # Search right half
        if arr[mid] < x:
            return binarySearch(arr, mid + 1, r, x, sorted=True)
        # Search left half
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x, sorted=True)
        # Element Found
        else:
            return mid

    return -1


# Default Test Case
# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x, True)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")

# ######################Additional Test Cases##########################
# (1) Sorted Array
arr = [2, 3, 4, 10, 40]
op = binarySearch(arr, 0, len(arr)-1, 2, True)
assert op == 0, f"Expected 0 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 3, True)
assert op == 1, f"Expected 1 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 4, True)
assert op == 2, f"Expected 2 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 10, True)
assert op == 3, f"Expected 3 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 40, True)
assert op == 4, f"Expected 4 as output but instead got {op}"

op = binarySearch(arr, 0, len(arr)-1, 0, True)
assert op == -1, f"Expected -1 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 5, True)
assert op == -1, f"Expected -1 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 100, True)
assert op == -1, f"Expected -1 as output but instead got {op}"

# (1) UnSorted Array
arr = [2, 40, 4, 3, 10]
op = binarySearch(arr, 0, len(arr)-1, 2)
assert op == 0, f"Expected 0 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 3)
assert op == 1, f"Expected 1 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 4)
assert op == 2, f"Expected 2 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 10)
assert op == 3, f"Expected 3 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 40)
assert op == 4, f"Expected 4 as output but instead got {op}"

op = binarySearch(arr, 0, len(arr)-1, 0)
assert op == -1, f"Expected -1 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 5)
assert op == -1, f"Expected -1 as output but instead got {op}"
op = binarySearch(arr, 0, len(arr)-1, 100)
assert op == -1, f"Expected -1 as output but instead got {op}"
# #######################################################################
