# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
'''
// Time Complexity : O(logN)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : little round about to get mid point


// Your code here along with comments explaining your approach
'''

'''
1. calc mid point on array repeat following until searched is found and right is greater than or equal to left
  2. if array value at mid is searched return
        array value is greater searched is left side so chop right part
        array value is smaller searched is right side , chop left side

'''
def bsi(arr,l,r,x):
  while True:
    mid=(l+r)//2

    if r>=l:
      if arr[mid]==x:
        return mid
      elif arr[mid]<x:
        l=mid+1
      else:
        r=mid-1
    else:
      return -1  
  
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ,55,67,89] 
x = [10,3,0,-4,67]
  
# Function call
def test(func):
  for to_be_find in x: 
    result=func(arr, 0, len(arr)-1, to_be_find)
    print(str(to_be_find)+' : '+str(result))

test(bsi)



