# Time Complexity : O (log n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this : No

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  # We will run thr while loop until our left pointer reaches or crosses our right pointer.
  # We use equals to symbol to make sure we search the complete array. 
  # If we use the condition l<r instead of l<=r, there will be one element left at l=r.
  while l<=r:
    
    # We will find the mid element of the array using the below formula.
    mid = l + (r-l)//2
    # We will check if the element at the mid value of the array is the element we need to find.
    if arr[mid] == x:
      # If yes, we will return the position of the element in the array by returning the mid value.
      return mid
    # If the value at the mid of the array is less than the value we need to find, 
    # we will shift the left pointer to the value that is next to mid as the array is sorted and the values
    # between the mid and left pointer will also be lesser than the value we need to find.
    elif arr[mid] < x:
      l = mid+1
    # If the value at the mid of the array is greater than the value we need to find, 
    # we will shift the right pointer to the value that is previous to mid as the array is sorted and the values
    # between the mid and right pointer will also be greater than the value we need to find.
    else:
      r = mid-1
  # If we don't find the element before we get out of the while loop, it means the element is not
  # present in the array. So, we return -1.
  return -1
  

  
  
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")
