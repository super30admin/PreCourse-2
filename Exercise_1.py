# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  '''
  1. Sort the array
  2. Find the middle element
  3. If middle element > the item to be searched then set the left = middle_index + 1
  4. If middle element < the item to be searched then set the right = middle_index - 1
  5. Repeat the steps 2 to 4 till we find the item or else return -1
  '''
  arr.sort()
  while l <= r:
    middle_index = (l + r) // 2
    if arr[middle_index] == x:
      return middle_index
    elif arr[middle_index] < x:
      l = middle_index + 1
    elif arr[middle_index] > x:
      r = middle_index - 1
  
  return -1
  
    
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 2
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print(f"Element is present at index {result}" )
else: 
    print("Element is not present in array")
