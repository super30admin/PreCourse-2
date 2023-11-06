# Python code to implement iterative Binary Search.
# It returns location of x in given array arr, if present, else returns -1
# Time Complexity is log O(log n). Space complexity is O(1).

def binarySearch(arr, l, r, x):
    while l <= r:
        mid = (l + r) // 2              # Find middle of the array

        if x > arr[mid]:                # Check if wanted value is greater than middle value
            l = mid + 1                 # Set l to be greater than middle value to continue search to the right of it
        elif x < arr[mid]:              # Check if wanted value is less than middle value
            r = mid - 1                 # Set r to be less than middle value to continue search to the left of it
        else:
            return mid                  # Check if wanted value is equal to middle value
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")