# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

#Time Complexity: O(log n)
#Space Complexity: O(1) [no extra space being used excpet for variables to store low, mid and high]
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while l<=r:
    #find the middle element
    mid = (l+r)//2
    if arr[mid] == x:
      # Check if middle element matches the key
      return mid
    elif x > arr[mid] :
      # If key is greater than the middle element, reduce the search range to indices higher than mid index
      l = mid + 1
    else:
      # If key is smaller than the middle element, reduce the search range to indices lower than mid index
      r = mid - 1
  return -1
    
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print(f"Element is present at index {result}") 
else: 
    print("Element is not present in array")
