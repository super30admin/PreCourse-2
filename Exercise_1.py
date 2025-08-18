# Python code to implement iterative Binary  
# Search. 

"""
TC: O(log(N)) {since after every function call, the search space reduces by half}
SC: O(1) {No extra space is being used}
"""
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  mid = l + (r-l)//2 #mitigating overflow issues, in case of very large numbers

  if arr[mid] == x:
    return mid

  if l==r:
     return -1

  if arr[mid] > x:
    return binarySearch(arr, l, mid-1, x)
  else:
    return binarySearch(arr, mid+1, r, x)
  

# Test array 
arr = [ 2, 3, 4, 10, 40] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print(f"Element is present at index {result}") 
else: 
    print(f"Element is not present in array")
