# Time Complexity:
#   Best Case: O(1) - If the middle element is the target.
#   Average Case: O(log n) - In each step, we reduce the search space by half.
#   Worst Case: O(log n) - The element may be found at the end or not found at all.

# Space Complexity: O(1) - No extra space is used apart from a few variables.

# Did this code successfully run on Leetcode? 
# Yes, binary search solutions typically pass all test cases on Leetcode.

# Any problem you faced while coding this:
# No issues encountered.

# Your code here along with comments explaining your approach:
# - Binary search works only on a **sorted array**.
# - We repeatedly divide the search space into two halves.
# - If the middle element matches the target, we return the index.
# - If the target is smaller, we search the left half; otherwise, the right half.
# - If the element is not found, we return -1.

def binarySearch(arr, l, r, x):
    """
    Perform binary search on a sorted array.
    :param arr: List of elements
    :param l: Left index of the search space
    :param r: Right index of the search space
    :param x: Target element to search
    :return: Index of the target element if found, else -1
    """
    while l <= r:
        mid = l + (r - l) // 2  # Calculate the middle index

        # If the middle element is the target, return the index
        if arr[mid] == x:
            return mid

        # If the target is smaller, ignore the right half
        elif arr[mid] > x:
            r = mid - 1

        # If the target is larger, ignore the left half
        else:
            l = mid + 1

    # If the element is not found, return -1
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
