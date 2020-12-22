'''
Binary Search

Time Complexity: O(logn)
Space Complexity: O(1)
Issue while implementing: No
'''



# Issue know binary search, but while implementing issues with ow to set the while loop.

def binarySearch(arr, l, r, x):
    mid = int(len(arr) / 2)
    while l <= r:
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid
            mid = l + int((r-l)/2)
        elif arr[mid] > x:
            r = mid
            mid = r -  int((r-l)/2)
        else:
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
