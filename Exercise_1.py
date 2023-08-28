# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  #Time Complexity: O(logn) Space Complexity: O(logn)
  #write your code here
   middle=int((l+r)/2)
   if arr[middle] == x :
      return middle
   elif arr[middle]> x and l is not r:
      r=middle-1
      return binarySearch(arr,l,r,x)
   elif arr[middle]<x and l is not r:
      l= middle+1
      return binarySearch(arr,l,r,x)
   else:
      return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 

result = binarySearch(arr, 0, len(arr)-1, x)
if result != -1: 
     print ("Element is present at index % d" %result) 
    
else: 
    print ("Element is not present in array")
