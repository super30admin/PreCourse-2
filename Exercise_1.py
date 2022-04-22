'''
Approach:

1. This is a binary search, so we will assume that our array is sorted (here ascending order)
2. We will perform recursion
3. We will pass the left boundary, right boundary and search the element in that boundary.
4. We will find th mid of the boundary, if 'x' matches the mid, return the index
5. If the value of x is less than mid, search on the lhs. Adjust the right boundary to mid-1
6. If the value of x is greater than mid, search on the rhs. Adjust the left boundary to mid+1
7. Our recursion stops if our left boundary is greater than right boundary.
8. Time Complexity:
   Since we are finding the mid and iterating the half of the list
   Our complexity will be 0(nlogn)
9. I faced the problem of infinite recursion call. On debug I realized that I need to adjust the boundary either by
    +1 or -1 to solve this problem
10. Didn't check on leet code, need leet code link to check it out
'''
# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
    
    if r < l:
        # It's invalid case
        return -1
    
    # 1. Find th mid pt
    mid = l + (((r-l)+1)//2)
    
    # 2. Compare
    if arr[mid] == x:
        # It's a match
        return mid
    
    elif arr[mid] >  x:
        # On the lhs of the list
        return binarySearch(arr, l, mid-1, x)
    
    elif arr[mid] < x:
        # On the rhs of the  list
        return binarySearch(arr, mid+1, r, x)
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10

# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 

  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")
