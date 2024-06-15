# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

"""
Time Complexity: O(log n)
Space Complexity: O(n)

"""

def search_loaction(arr, mid, x):
    if arr[mid] == x:
        return 'found'
    elif arr[mid] < x:
        return 'right'
    elif arr[mid] > x:
        return 'left'
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while l <= r:
      mid = (l+r) // 2
      result = search_loaction(arr, mid, x)
      
      if result == 'found':
          return mid
      elif result == 'right':
          l = mid+1
      elif result == 'left':
          r = mid - 1
  return -1

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 2
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print(f"Element is present at index {result}")
else: 
    print("Element is not present in array")
