# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity = O(logn)
# Space Complexity = O(1)
# Any problem you faced while coding this : No
# 
def binarySearch(arr, l, r, x): 
   while l <= r:
       # Calculating middle position
       mid = l + (r -l) //2 
       # If value we are looking for is at mid we will return it
       if arr[mid] == x:
           return mid
       # if mid is greater than x shift right pointer to mid -1
       elif arr[mid] > x:
           r = mid - 1
       else:
           l = mid + 1
   # returning -1 if value is not present in sorted array
   return -1
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print ("Element is not present in array")
