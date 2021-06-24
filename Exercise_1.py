# Python code to implement iterative Binary  
# Search. 
#Time Complexity :  O(logn)
#Space Complexity : O(1)
#Did this code successfully run on Leetcode : yes
#Any problem you faced while coding this : no

def binarySearch(arr, l, r, x): 
    if r>=l: 
        mid = l + (r-l)//2
        if arr[mid]==x:
            return mid
        elif x < arr[mid]:
            return binarySearch(arr,l,mid-1,x)   # search in lower half of
                    
        else:
            return binarySearch(arr,mid+1,r,x)
                
    else:
        return -1		

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 50
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
     print ("Element is present at index {}".format(result ))
else: 
    print( "Element is not present in array")
