# Time Complexity :   O(Log N)
# Space Complexity :  O(1)
# Did this code successfully run on Leetcode :

# Any problem you faced while coding this :

# Your code here along with comments explaining your approach

def binarySearch(arr, l, r, x):
    while(r>=l):
        mid= (r+l)//2
        if(arr[mid]==x):
            return mid
        if(arr[mid]<x):
            l=mid+1
        else:
            r=mid-1
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
