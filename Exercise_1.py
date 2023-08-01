# Time Complexity : O(logn) where n is the number of elements in the input array
# Space Complexity : O(1) since it uses constant amount of extra space. Space is not dependent on the length of input array

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  while l<=r:
    mid = l+(r-l)//2 #We find the middle index using the formula. Used //  to prevent interger overflow.
    if arr[mid] == x: #Check if the middle element is the target element
      return mid #If true, return the middle index
    elif arr[mid] < x: #Since the array is sorted in ascending order (must for Binary Search), we check if the middle element if smaller than target element or no
      l = mid+1 #If true, we change the left boundary to middle index + 1
    else:
      r = mid-1 #If false, we change the right boundary to middle index - 1
  return -1 #Return -1 if the element is not present in the array
  
# Test array (Note: The array must be sorted in ascending order for Binary Search)
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")
