# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time and Space Complexity
# Time Complexity is O(log N) where N is the nuber of elements that are present in the given arr
# Space Complexity is O(1) as the variables are constant irrespective of the array size
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while l<=r:
     mid=(l+r)//2
     if arr[mid]==x:
        return mid
     elif x<arr[mid]:
        r=mid-1
     else:
        l=mid+1
  
  return -1 
      
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result)
else: 
    print ("Element is not present in array")
