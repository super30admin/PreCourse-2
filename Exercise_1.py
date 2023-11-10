
# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity : O(log(n))
# Space Complexity : O(1), uses 2 pointers of memory only, to check code, aka same amnt of space regardless of input
# Did this code successfully run on Leetcode : Yes,
# Any problem you faced while coding this : variable spelling error,
# incrementing midpoint vs moving the l and r + 1.

"""BS works in logN, divides work each time""" 
def binarySearch(arr, l, r, x): 

  #write your code here
  #thinking of for lop since its iterative...
  # midpoint prevent binary search overflow and // rounds down

  #Dont use for loop when you can use while!
  #loop til search space exhausted
  while l <= r:
    midpoint = (r+ (r - l)) // 2
    if arr[midpoint] == x:
      return midpoint
    elif x > arr[midpoint]:
      l = midpoint + 1
    else:
      r = midpoint - 1

  #else location of x is NOT present, -1
  return -1
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")
#took 50min to answer this problem