# Python code to implement iterative Binary Search. 
# It returns location of x in given array arr  
# if present, else returns -1 
#time complexity: O(log n)
#space complexity: O(1)
def binarySearch(arr, l, r, x): 
  while r>=l:
    mid = int((r+l)/2)
    if arr[mid] > x:     #if x is smaller, search in left half of array and ignore right portion
        r = mid-1
    elif arr[mid] < x:   #if x is greater, search in right half and ignore left portion
        l = mid+1
    else:                #if x is at middle
        return mid
  return -1              #x is not present in array
   
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print(f"Element is present at index {result}")
else: 
    print("Element is not present in array")
