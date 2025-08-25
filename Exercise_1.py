# Time Complexity : O(log(base 2)(N))
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Could not find the problem on leetcode
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach
# We can use Binary Search when the array is sorted. It reduces the search time of O(N) i.e. linear to O(log(base 2)(N)) i.e. logarithmic
# I am assuming the input array on which we are applying the Binary Search would always be sorted
# Reducing the search space by half on every iteration

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  if((len(arr) == 0) or (not (0 <= l <= len(arr)-1)) or (not (0 <= r <= len(arr)-1)) or (x < arr[0]) or (x > arr[-1])):
     return -1
  
  while(l <= r):
     mid = ((2 * r) - (r - l)) // 2
     if(x == arr[mid]):
        return mid
     elif(x < arr[mid]):
        r = mid - 1
     else:
        l = mid + 1

  return -1
        
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x)
if result != -1: 
    print("Element is present at index %d" % result) 
else: 
    print("Element is not present in array")

result = binarySearch(arr, 0, len(arr)-1, 0)
if result != -1: 
    print("Element is present at index %d" % result) 
else: 
    print("Element is not present in array")

result = binarySearch(arr, 0, len(arr)-1, 50)
if result != -1: 
    print("Element is present at index %d" % result) 
else: 
    print("Element is not present in array")

result = binarySearch(arr, 0, len(arr)-1, 6)
if result != -1: 
    print("Element is present at index %d" % result) 
else: 
    print("Element is not present in array")

result = binarySearch(arr, 0, len(arr)-1, 2)
if result != -1: 
    print("Element is present at index %d" % result) 
else: 
    print("Element is not present in array")

result = binarySearch(arr, 0, -1, 2)
if result != -1: 
    print("Element is present at index %d" % result) 
else: 
    print("Element is not present in array")

result = binarySearch(arr, len(arr), 3, 2)
if result != -1: 
    print("Element is present at index %d" % result) 
else: 
    print("Element is not present in array")

