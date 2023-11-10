# Time Complexity : O(logN), because binary search
# Space Complexity : O(N), for length of array.
# Did this code successfully run on Leetcode : Yes, it did. 
# Any problem you faced while coding this : Took a couple of attempts. 
# Had to test and redo. 


# Your code here along with comments explaining your approach

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 

    #write your code here
    #Assumes array is sorted in ascending order already.
    #If x is less than the smallest or greater than largest in arr.
    if arr[l]>x or arr[r]<x:
        return -1
    #if x is within the range of (smallest, largest), use recursion. 
    if arr[l]<=x and arr[r]>=x:
        #if diff between two points is 1 or 0.
        if r-l<=0:
            if arr[l]==x:
                return l
            elif arr[r]==x:
                return r
            else:
                return -1
        else:
            # find mid and recurse on left arr and right arr. 
            mid = int((l+r)/2)
            left = binarySearch(arr, l, mid, x)
            right = binarySearch(arr, mid+1, r, x)
            if left ==-1 and right==-1:
                return -1
            elif left==-1:
                return right
            else:
                return left


# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10

# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
    print(f"Element is present at index {result}.") 
else: 
    print("Element is not present in array")
