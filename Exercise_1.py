"""
Time Complexity : O( log(n) )
Space Complexity : O(n)
Did this code successfully run on Leetcode : N/A
Any problem you faced while coding this : No
"""

# Python code to implement iterative Binary
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
    '''
    finding mid-point of array and comparing its value with value to be found.
    Then iterating over either left or right part of mid-point depending on value of mid and value to be found.
    :param arr: sorted array
    :param l: lower bound
    :param r: higher bound
    :param x: value to found
    :return: position of value
    '''
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            l = mid+1
        elif x < arr[mid]:
            r = mid-1
    return -1

  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
