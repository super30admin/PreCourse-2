# Exercise_1 : Binary Search

# Assumption: Array is sorted in ascending order
# Time Complexity: O(log N), N = number of elements in array
# Space Complexity: O(1), since we use the same array to store the sorted elements
# Successful Run on Leetcode: Yes (https://leetcode.com/problems/binary-search/)
# Challenges: None

# It returns location of x in given array arr if present, else returns -1 
def binarySearch(arr, l, r, x): 
  # using the left and right pointers, keep checking the middle element
  while l <= r:
    mid = (l + r) // 2
    # if the middle element is the target, return the index
    if arr[mid] == x:
      return mid
    # if the middle element is less than the target, move the left pointer to the right of the middle element
    elif arr[mid] < x:
      l = mid + 1
    # if the middle element is greater than the target, move the right pointer to the left of the middle element
    else:
      r = mid - 1
  # if the target is not found, return -1
  return -1
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index", result)
else: 
    print("Element is not present in array")
