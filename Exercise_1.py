# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

#Time Complexity O(logn)
#Auxilary Space Complexity O(logn)
#Accesing the mid element in an array and if required number is mid will return index
#if value is less than mid then search only in left subarray else search in right subarray
def binarySearch(arr, l, r, x): 
  
  #write your code here
  if l <= r:
    mid = (l + r)//2
    if arr[mid] == x:
      return mid
    else:
      if arr[mid] > x:
        return binarySearch(arr,l,mid-1,x)
      else:
        return binarySearch(arr,mid+1,r,x)
  return -1
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result )
else: 
    print("Element is not present in array")
