# Python code to implement iterative Binary  
# Search. 

#Time complexity - O(logn)
#space complexity - O(1) 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  #recursive binary search
  #checking base case 
  if r>=l:
    #finding the mid-point 
    mid=l+(r-l)//2
    #if element found return index
    if arr[mid]==x:
      return mid
    #if element is smaller than mid element, then element will be present in left subarray
    elif arr[mid]>x:
      return binarySearch(arr,l,mid-1,x)
    #if element is larger than mid element, then element will be present in right subarray
    else:
      return binarySearch(arr,mid+1,r,x)
  #if base condition fails , return -1 (element not found)
  else:
    return -1



  
  

  
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")
