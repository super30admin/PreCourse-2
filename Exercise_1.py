# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  
    while l<=r:
          mid = l + (r-l) // 2
          if arr[mid] < x:
                l = mid + 1
          elif arr[mid] > x:
                r = mid - 1
          else:
                return mid
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

# Time Complexity :  O(logN)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : yes (704 binary search)
# Any problem you faced while coding this :  
# Minor issue like using brackets for print statement if i use python3 instead of python2 and
# using l + (r-l) // 2 instead of l + r // 2 

# Your code here along with comments explaining your approach:
# The idea is to repeatedly divide the search space in half.
# - Start with the whole array.
# - If the middle element is equal to the target, return the index.
# - If the target is less, search the left half (r = mid - 1).
# - If the target is more, search the right half (l = mid + 1).
# - Continue this until the range is empty.
# This approach avoids recursion and runs in O(log n) time.