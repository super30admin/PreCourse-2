# Python code to implement iterative Binary  
# Search. 

# It returns location of x in given array arr  
# if present, else returns -1 

# // Time Complexity : O(logn)
# // Space Complexity : O(logn)

def binarySearch(arr, l, r, x): 
   #write your code here
   while l <= r:
    mid = l + (r - l) // 2    
    if  x == arr[mid]:
      return mid
    if x < arr[mid]:
      r = mid - 1
    else:
      l = mid + 1
   return -1    

 
      
      
x=10
arr = [ 2, 3, 4, 10, 40 ] 
result = binarySearch(arr, 0, len(arr)-1, x) 
if result != -1: 
    print "Element is present at index % d" % result 
    print ("Element is present at index % d" % result )
else: 
    print "Element is not present in array"
    print ("Element is not present in array")
  
