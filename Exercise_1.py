# Python code to implement iterative Binary Search. 
# Time Complexity : O(log n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : No. Could not find this problem(with 4 argument) on geeks or leetcode
# Any problem you faced while coding this : No

# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  # write your code here
  # sorting the given array
  arr.sort()

  # finding the middle index
  mid_index = int((l + r) / 2)
  # checking if middle is equal to given element
  if x == arr[mid_index]:
    return mid_index
  
  # checking if the given element is grater than middle element
  elif (x > arr[mid_index]):
    return binarySearch(arr, mid_index+1, r, x)
    
  # checking if the given element is less than middle element
  elif (x < arr[mid_index]):
    return binarySearch(arr,l ,mid_index-1, x)
  
  return -1
  
# Test array 
arr = [2, 3, 4, 10, 40] 
x = 3
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
    print("Element is present at index", result)
else: 
    print("Element is not present in array")