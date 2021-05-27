# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
    mid = (l+r)//2  
    if x == arr[mid]:
      return mid
    elif x > arr[mid]:
      return binarySearch(arr, mid, r, x)
    elif x < arr[l+r//2]:
      return binarySearch(arr, 0, mid, x) #as binarySearch is returning a value add return keyword before recursive call
    return -1
  
  
  

  
  #write your code here
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index %d" % result)
else: 
    print("Element is not present in array")
