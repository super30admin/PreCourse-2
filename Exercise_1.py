'''
Time Complexity : O(log(n))
Space Complexity : O(1) 
'''
# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  #write your code here
  while(r>=l):
    mid = int((l+r)/2)
    if(arr[mid]==x):
      return mid
    elif(arr[mid]>x):
      r = mid-1
    else:
      l = mid+1
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
