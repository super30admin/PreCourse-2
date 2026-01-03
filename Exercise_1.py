# Python code to implement iterative Binary  
# Search will use pointers left pointer will start at 0th index and right pointer will start at last index
# of the array and we use while loop to find the target element
# while condition will make sure the left and right pointer dont cross each other
# calcuate the middle and check if the middle index value is greater or smaller than the target
# if middle value is greater than the target then then point the right pointer to mid - 1 or else point left to mid + 1
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):

  while l <= r:
    mid = (l + r) // 2

    if arr[mid] == x:
      return mid
    elif arr[mid] > x:
      r = mid - 1
    else:
      l = mid + 1
  return -1  
    
  
# Test array 
# arr = [ 2, 3, 4, 10, 40 ]
arr = [1, 2, 9]
x = 9
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
