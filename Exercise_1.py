# Time Complexity: O(log n)

# Space Complexity: O(1)


# Python code to implement iterative Binary  
# Search. 
 
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while l <= r:
        mid = l + (r - l) // 2  # Calculate the middle index safely to avoid overflow.
        if arr[mid] == x: # If the middle element is the target, return its index
            return mid
        elif arr[mid] < x:# If target is greater than mid element, ignore left half
            l = mid + 1
        else: # If target is smaller than mid element, ignore right half
            r = mid - 1
  return -1 # If the element is not found in the array, return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")
