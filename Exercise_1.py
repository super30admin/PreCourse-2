"""
Runtime Complexity:
O(log n)- The algorithm works by taking the middle element of the array and slices it into two halves, left and right. Then we compare and check whether the target 
element is in the left half or right half. If target is lesser than mid then we search the left half else we search right half iteratively. Since the iteration goes on ,
the elements are stores in log levels. This forms a iteration tree. Length of 'n' node tree is log n. Therefore the overall time complexity is O(log n)

Space complexity:
O(1) - we just compare and assign mid. These operations take O(1) space .

Yes, it worked on leetcode.
"""

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
    while l<=r:
        mid = l+(r-l)//2
        
        if arr[mid] ==x:
            return mid
        elif arr[mid]<x:
            l = mid+1
        else: 
            r =mid-1
    return -1

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")
