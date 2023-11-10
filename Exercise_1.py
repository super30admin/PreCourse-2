# Python code to implement iterative Binary Search. 

#Time complexity : O(log(n))
#Space complexity : O(1)
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  #write your code here
  mid = 0

  while l <= r:
    mid = (l + r)//2
    mid_number = arr[mid]

    if mid_number == x:
      return mid
    
    if mid_number < x:
      l = mid + 1

    else:
      r = mid + 1
  return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 3
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
