# Python code to implement iterative Binary
# Search.

# Time: O(log N)
# Space: O(1)

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):
  #write your code here
  mid = int((l+r)/2)

  if l > r:
     return -1

  if x == arr[mid]:
    index = mid
  elif x > arr[mid]:
    index = binarySearch(arr, mid+1, r, x)
  else:
    index = binarySearch(arr, l, mid-1, x)
  return index

# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
