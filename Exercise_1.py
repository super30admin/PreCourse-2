# Python code to implement iterative Binary Search.
# Time Complexity : O(log n)
# Space Complexity : O(1) as it is iterative
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : None

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr,l, r, x):

  #write your code here
  low = l
  high = r
  Found = False
  while low <= high and not Found:
      mid = (low + high) // 2
      if x == arr[mid]: # checking if key is equal to our mid value
          Found == True  # element found
          return mid
      elif x < arr[mid]: # checking if key is less than our mid value
          high = mid - 1
      else:
          low = mid + 1 # checking if key is greater than our mid value

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
