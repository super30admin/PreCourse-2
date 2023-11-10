# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  #write your code here
  
  if l>r:
    return -1

  mid = (l+r)//2
  if x==arr[mid]:
    return mid
  
  if x<arr[mid]:
    return binarySearch(arr,l,mid-1,x)
  
  if x>arr[mid]:
    return binarySearch(arr,mid+1,r,x)
  
 
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 1
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index")
else: 
    print("Element is not present in array")
