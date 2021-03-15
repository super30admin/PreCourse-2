# Python code to implement iterative Binary  
# Search. 
''' Time complexity : O(log n)
Space Complexity: O(1)


Did this code successfully run on Leetcode : 
Any problem you faced while coding this : No ''' 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
    while l <= r: 
  
        mid = l + (r - l) // 2; 
          
        #if element is in mid
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, go with right half
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, go with left half 
        else: 
            r = mid - 1
      
    #element not present
    return -1
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")
