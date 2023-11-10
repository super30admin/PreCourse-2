# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1

# Time Complexity : O(log n)
# Space Complexity : O(1)
# Any problem you faced while coding this : No
# The code finds the middle of the array and compares if x is larger or smaller than the middle, then it finds a new middle and repeats until x is found
def binarySearch(arr, l, r, x):
  m = 0
  while l <= r:
      m = (r + l)//2
      if arr[m] < x:
          l = m + 1
      elif arr[m] > x:
          r = m - 1
      else:
          return m
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
