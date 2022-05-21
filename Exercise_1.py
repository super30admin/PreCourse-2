# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 


# Time Complexity : O(log n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

def binarySearch(arr, l, r, x): 
  
  #write your code here
  
  while l<=r:
      #Find the midpoint
      mid=(l+r)//2
      
      #Check if the element to be searched is the middle element or not and return the if yes
      if arr[mid]==x:
          return mid
      #else check where the element could lie, on the left side or at the right side
      elif x > arr[mid]:
          l=mid+1
      else:
          r=mid-1
  #return -1 if element is not present in the list
  return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index: ",result)
else: 
    print ("Element is not present in array")
