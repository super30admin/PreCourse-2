# Python code to implement iterative Binary Search. 
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity : O(logn) - as the steps taken to reach the answer is logn, as at every step, the n is reduced by half.
# Space Complexity : O(1) - No additional space is used
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Not really

# We take a low(0), high(n-1) and mid as pointers to the index, find the mid, if the element at mid is same as target, we return the mid, if the target is less than arr[mid], then we need to search in the left, hence we do high = mid -1
# If the target is greater than arr[mid], we need to search in the right side of array, hence we do low = mid+1

def binarySearch(arr, l, r, x): 
  
  #write your code here

  mid = (l+r)//2
  while l<=r:
     mid = (l+r)//2
     if arr[mid] == x:
        return mid
     elif x > arr[mid]:
        l = mid + 1
     else:
        r = mid - 1
  return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10 , 10, 10, 10] 
x = 10

# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print(f"Element is present at index {result}") 
else: 
    print("Element is not present in array")
