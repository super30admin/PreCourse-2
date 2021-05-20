# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity : log(n)
# Space Complexity : O(1) No extra space used
# Approach: Find the mid element of the array. 
# 1. If the mid element is equal to the key, return position of mid
# 2. If the key is smaller than mid element, find key in the left subarray otherwise right subarray. 
# 3. Update left and right subpointers accordingly and continue with loop until left < right.
def binarySearch(arr, l, r, x): 
  
  while(l < r):
    mid = l + (r - l) // 2;
    if arr[mid] == x:
      return mid
    elif arr[mid] < x:
      l = mid + 1
    else:
      r = mid - 1
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
