#Time Complexity :  O(logn)
#Space Complexity : O(1)
#Did this code successfully run on Leetcode : yes
#Any problem you faced while coding this : no

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while l<=r:
    #compute mid
    mid=(l+r)//2
    # case 1
    if arr[mid]==x:
      return mid
      # case 2
    elif x>arr[mid]:
      l=mid+1
      #case 3
    else:
      r=mid-1
  return -1


    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")