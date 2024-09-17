# Python code to implement iterative Binary  
# Search. 

# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr: list, left: int, right: int, x: int) -> int:
    """
        'n' is the length of the array
        Time Complexity: O(logn)
        Since we are cutting down the size by half at each level
        Space Complexity: O(logn)
        Since the maximum function calls we make is when the number to be searched is the left most or right most
        and at that point we would have logn functions in the stack.
    """
    # Base case
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    # element is present in right half
    if arr[mid] > x:
        right = mid - 1
    # element is present in left half
    if arr[mid] < x:
        left = mid + 1
    return binarySearch(arr, left, right, x)


if __name__ == '__main__':
    # Test array
    arr = [2, 3, 4, 10, 40]
    x = 100

    # Function call
    result = binarySearch(arr, 0, len(arr) - 1, x)

    if result != -1:
        print(f'Element is present at index {result}')
    else:
        print('Element is not present in array')
