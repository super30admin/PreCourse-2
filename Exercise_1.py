# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1


    
      

def binarySearch(arr, l, r, x): 
  
  #write your code here
  mid = l+(r-l)//2
  #print(mid)

  if arr[mid]==x:
    return mid
  else:
    if arr[mid] > x:
      return binarySearch(arr,l,mid,x)
    else:
      return binarySearch(arr,mid+1,r,x)
  return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 2
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")

#TC: O(LogN)
#SC: Recursion takes memory for stack : O(LogN)