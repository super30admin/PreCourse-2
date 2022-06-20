'''
# Exercise_1 : Python code to implement Binary Search.

# Description: Binary search algorithm.
               It returns location of x in given array arrary if present, else returns -1

# Author: Neha Doiphode
# Date  : 06-17-2022

# Approach:
    * Binary search uses divide and conquer technique.
    * Requirement is to have input array sorted.
    * Technique finds middle element of the sorted array and compares the key to be searched with the middle element.
    * If key is less than middle, the search focuses only on the left half of the middle.
      else, it focuses on the right half of the middle and so on until the element is found or the search space is exhausted.


# Time Complexity                            : O(log n)
#                                              Since at each iteration the search space is reduced by half,
#                                              if we consider, length of array = n, at each subsequent iteration it will be,
#                                              n, n/2, n/4, n/8, n/16,.........n/2^k.
#                                              After k iterations array size will be reduced to 1.
#                                              Hence, n/2^k = 1 which is nothing but k = log n(base 2).

# Space Complexity                           : O(1), no auxiliary space is required.

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this    : Nothing critical.
'''

def binarySearch_iterative(arr, l, r, x):
    while l <= r:
        mid = int((l + r) / 2)

        if x < arr[mid]:
            r = mid - 1
        elif x == arr[mid]:
            return mid
        else:
            l = mid + 1

    return -1

def binarySearch_recursive(arr, l, r, x):
    # Exit condition
    if l > r:
        return -1
    else:
        mid = (l + r) // 2

        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            return binarySearch_recursive(arr, l, mid - 1, x)
        else:
            return binarySearch_recursive(arr, mid + 1, r, x)
    return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binarySearch_iterative(arr, 0, len(arr)-1, x)

print()

print('Approach 1: Binary search - Iterative.')
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")

print()
print()

result = binarySearch_recursive(arr, 0, len(arr)-1, x)
print('Approach 2: Binary search - Recursive.')
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")

print()
