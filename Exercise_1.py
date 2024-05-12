# Python code to implement iterative Binary  
# Search. 

# Time complexity O(log n)
# Space compexity O(1)
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  # write your code here
  mid = 0

  while l < r:
     
     mid = (l + r) // 2
     
     # If x is greater than middle element ignore left half
     if arr[mid] < x:
        l = mid + 1

     # If x is less than middle element ignore right half   
     elif arr[mid] > x:
        r = mid - 1

     # x is a middle element   
     else:
        return mid
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
