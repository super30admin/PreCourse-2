# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  # The Binary Search function checks whether an element exists in a given array by utilizing the left 
  # and right pointers of the array and updating them based on specific criteria.
  while l<=r:
     mid = (l+r)//2
     if arr[mid] == x:
        return mid
     elif arr[mid] < x:
        l = mid +1
     else:
        r = mid -1  
  return -1 
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 4
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index ", result)
else: 
    print ("Element is not present in array")
