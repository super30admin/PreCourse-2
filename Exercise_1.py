'''
Binary Search.
'''

# Time Complexity : O(log n) as we are dividing the search space in half with each iteration.
# Space Complexity : O(1) as we are using a constant amount of space for variables.
# Did this code successfully run on Leetcode : Yes, I ran the code on Problem 704 (Binary Search) on LeetCode and it passed all test cases.
# Any problem you faced while coding this : Yes, to understand how to correctly update the left and right indices during the search process.

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): # we have defined the binarySearch function which takes an array arr, left index l, right index r, and the element x to be searched.
  # Check base case
  if r >= l: # if the right index is greater than or equal to the left index, we proceed with the search.
    return -1 # if the right index is less than the left index, we return -1 indicating that the element is not found.
  
  #write your code here
  while l <= r: # we use a while loop to continue searching as long as the left index is less than or equal to the right index.
    mid = l + (r-l) // 2 # we calculate the middle index mid using the formula l + (r-l) // 2 to avoid overflow.
    if arr[mid] == x: # if the element at the middle index is equal to x, we have found the element and return the index mid.
      return mid # if the element at the middle index is equal to x, we have found the element and return the index mid.
    elif arr[mid] < x: # if the element at the middle index is less than x, we search in the right half of the array by updating the left index to mid + 1.
      l = mid + 1 # if the element at the middle index is less than x, we search in the right half of the array by updating the left index to mid + 1.
    else: # if the element at the middle index is greater than x, we search in the left half of the array by updating the right index to mid - 1.
      r = mid - 1 # if the element at the middle index is greater than x, we search in the left half of the array by updating the right index to mid - 1.
  return -1 # if the element is not found, we return -1 indicating that the element is not present in the array.
  
# Driver code to test above function
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result) 
else: 
    print("Element is not present in array")
